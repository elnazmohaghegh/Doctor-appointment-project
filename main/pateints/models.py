from django.db import models
from django.contrib.auth.models import User
from home.models import Insurance

# Create your models here.


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    f_name = models.CharField(max_length=50, blank=True, null=True)
    l_name = models.CharField(max_length=100, null=True, blank=True)
    ins_type = models.ForeignKey(Insurance, on_delete=models.SET_NULL, null=True, blank=True, related_name='ins_type')
    national_code = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    illness_records = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.f_name + ' ' + self.l_name


