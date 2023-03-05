from django.contrib import admin
from .models import *

# Register your models here.


class DoctorTimeInline(admin.TabularInline):
    model = DoctorTime
    fields = ('day', 'date', 'start_time', 'end_time')
    extra = 10


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'takhasos', 'nezam_pezeshki', 'phone_number')
    inlines = [DoctorTimeInline]


class DoctorTimeAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'start_time', 'end_time')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'doctor', 'rate', 'create')


admin.site.register(Comment, CommentAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(DoctorTime, DoctorTimeAdmin)
