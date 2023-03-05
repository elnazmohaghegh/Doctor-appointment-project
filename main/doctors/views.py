from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Doctor
from visit.models import VisitsReserved
from home.models import Insurance
import ghasedak
from django.http import HttpResponse
import requests
from django.db.models import Q
import json
from django.contrib.auth.decorators import login_required
import jdatetime

# Create your views here.


def login_doctor(request):
    if request.method == 'POST':
        form = LoginDoctorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            myuser = authenticate(request, username=data['username123'], password=data['password'])
            if myuser:
                login(request, myuser)
                messages.success(request, 'ورود موفقیت امیز بود', 'success')
        return redirect('home:doctors_list')
    else:
        form = LoginDoctorForm()

    return render(request, 'doctors/login_doctor.html', {'kilideform': form})


@login_required(login_url='patients:p_login')
def doctor_details(request, id):
    doctor_info = Doctor.objects.get(id=id)
    doctor_times = doctor_info.doctor_times.all()
    ins_type = request.user.patient_profile.ins_type.id
    comment_form = CommentForm()
    comments = Comment.objects.filter(doctor_id=id)
    now_date = jdatetime.datetime.now().date()
    tomorrow = jdatetime.datetime.now().date() + jdatetime.timedelta(days=1)
    day_2 = jdatetime.datetime.now().date() + jdatetime.timedelta(days=2)
    day_3 = jdatetime.datetime.now().date() + jdatetime.timedelta(days=3)
    day_4 = jdatetime.datetime.now().date() + jdatetime.timedelta(days=4)

    return render(request, 'doctors/details.html', {'doctor': doctor_info, 'dr_times': doctor_times,
                                                    'ins_type': ins_type, 'comment_form': comment_form,
                                                    'comments': comments, 'now': now_date, 'tomorrow': tomorrow,
                                                    'day_2': day_2, 'day_3': day_3, 'day_4': day_4})


def reserve(request, id, ins_type):
    if request.method == 'POST':
        time = request.POST['time']
        ins = Insurance.objects.get(id=ins_type)
        dr = Doctor.objects.get(id=id)
        cost = ((100 - ins.percentage) / 100) * dr.dr_cost
        visit = VisitsReserved.objects.create(patient_id=request.user.patient_profile.id, doctor_id=dr.id, reserved_time_id=time,
                                      ins_type_id=ins_type, cost=cost)

        message = "رزرو شد" + '\n' + 'کد رهگیری شما: ' + str(visit.peygiri)
        receptor = "09158185056"
        linenumber = "10008566"
        sms = ghasedak.Ghasedak("")
        sms.send({
            'message': message,
            'receptor': receptor,
            'linenumber': linenumber
        })
        return redirect('doctors:check_reserve', visit.id)
    else:
        ins = Insurance.objects.get(id=ins_type)
        dr = Doctor.objects.get(id=id)
        cost = ((100 - ins.percentage) / 100) * dr.dr_cost

    return render(request, 'doctors/reserve.html', {'cost': cost, 'dr': dr})


def check_reserve(request, visit_id):
    visit = VisitsReserved.objects.get(id=visit_id)

    return render(request, 'doctors/check_reserve.html', {'visit': visit})



MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
amount = 11000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://localhost:8000/verify/'


def send_request(request):
    req_data = {
        "merchant_id": MERCHANT,
        "amount": amount,
        "callback_url": CallbackURL,
        "description": description,
        "metadata": {"mobile": mobile, "email": email}
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)
    authority = req.json()['data']['authority']
    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


def verify(request):
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                return HttpResponse('Transaction success.\nRefID: ' + str(
                    req.json()['data']['ref_id']
                ))
            elif t_status == 101:
                return HttpResponse('Transaction submitted : ' + str(
                    req.json()['data']['message']
                ))
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(
                    req.json()['data']['message']
                ))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user')


def comment_user(request, dr_id):
    if request.method == 'POST':
        url = request.META.get('HTTP_REFERER')
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(user_id=request.user.id, doctor_id=dr_id, comment=data['comment'], rate=data['rate'])
            messages.success(request, 'commented successfully', 'success')
            return redirect(url)


def dr_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            found = Doctor.objects.filter(Q(l_name__contains=data['search'])|Q(takhasos__contains=data['search']))

            return render(request, 'doctors/doctors.html', {'found': found})


def all_doctors(request):
    all_drs = Doctor.objects.all()

    return render(request, 'doctors/doctors.html', {'found': all_drs})
