import jdatetime
from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from pateints.models import Patient

# Create your models here.


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='doctor_profile')
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=100)
    takhasos = models.CharField(max_length=100)
    info = models.TextField()
    address = models.CharField(max_length=400)
    nezam_pezeshki = models.PositiveIntegerField()
    phone_number = models.PositiveIntegerField()
    dr_cost = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='doctors_images', null=True, blank=True)

    def __str__(self):
        return self.f_name + ' ' + self.l_name


class DoctorTime(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_times')
    day = models.CharField(max_length=50, null=True, blank=True)
    date = jmodels.jDateField(null=True, blank=True)
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)
    reserved = models.BooleanField(default=False)


    def __str__(self):
        return self.doctor.f_name + ' ' + self.doctor.l_name + ' ' + self.day + ' ' + self.start_time


class Comment(models.Model):
    user = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='comments_patient')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_comments')
    create = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    rate = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.user.f_name + ' ' + self.user.l_name