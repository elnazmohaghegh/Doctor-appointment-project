from django.shortcuts import render, redirect
from .forms import PatientRegisterForm, LoginUserForm
from django.contrib.auth.models import User
from .models import Patient
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from visit.models import VisitsReserved

# Create your views here.


def p_signup(request):
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ins = request.POST['insurance_type']
            myuser = User.objects.create_user(username=data['username1'], email=data['email1'], password=data['password2'])
            Patient.objects.create(user=myuser,f_name=data['f_name1'], l_name=data['l_name1'], national_code=data['national_code1'],
                                   phone_number=data['phone_number1'], ins_type_id=ins)
            messages.success(request, 'ثبت نام شدید', 'success')
            return redirect('home:doctors_list')
    else:
        form = PatientRegisterForm()

    return render(request, 'patients/signup.html', {'form':form})


def p_login(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            myuser = authenticate(request, username=data['username1'], password=data['password1'])
            if myuser:
                login(request, myuser)
                messages.success(request, 'vorood shod', 'success')
                return redirect('home:doctors_list')
            else:
                messages.warning(request, 'etelaat eshtebah', 'danger')
    else:
        form = LoginUserForm()

    return render(request, 'patients/login.html', {'form': form})


def user_profile(request):
    profile = request.user.patient_profile

    return render(request, 'patients/profile.html', {'profile': profile})


def reserved_visits(request):
    reservs = request.user.patient_profile.reserved_patient.all()

    return render(request, 'patients/reserved_times.html', {'reservs': reservs})


def user_logout(request):
    logout(request)

    return redirect('home:doctors_list')