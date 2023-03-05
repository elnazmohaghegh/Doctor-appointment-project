from django.shortcuts import render
from django.http import HttpResponse
from doctors.models import Doctor

# Create your views here.


def doctors_list_view(request):
    doctors_list1 = Doctor.objects.all()

    return render(request, 'home/home.html', {'doctors': doctors_list1})
