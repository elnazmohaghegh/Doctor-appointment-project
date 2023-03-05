from django.contrib import admin
from .models import Patient

# Register your models here.


class PatientAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'national_code', 'phone_number')


admin.site.register(Patient, PatientAdmin)