from django.contrib import admin
from .models import Insurance

# Register your models here.


class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


admin.site.register(Insurance, InsuranceAdmin)
