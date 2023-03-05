from django.contrib import admin
from .models import VisitsReserved

# Register your models here.


class VisitsReservedAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'day', 'start_time', 'end_time', 'peygiri', 'cost', 'ins_type')


admin.site.register(VisitsReserved, VisitsReservedAdmin)
