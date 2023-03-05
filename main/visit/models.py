from django.db import models
from pateints.models import Patient
from doctors.models import Doctor, DoctorTime
from home.models import Insurance
from random import randint
from django_jalali.db import models as jmodels

# Create your models here.


def random_code():
    return randint(100000, 999999)


class VisitsReserved(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reserved_patient')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='reserved_doctor')
    reserved_time = models.ForeignKey(DoctorTime, on_delete=models.CASCADE, related_name='reserved_date', null=True, blank=True)
    day = jmodels.jDateField(null=True, blank=True)
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)
    ins_type = models.ForeignKey(Insurance, on_delete=models.SET_NULL, null=True, blank=True)
    cost = models.PositiveIntegerField()
    peygiri = models.PositiveIntegerField(default=random_code)

    def __str__(self):
        return self.patient.f_name + ' ' + self.patient.l_name