from django.urls import path
from .views import *


app_name = 'doctors'

urlpatterns = [
    path('login/', login_doctor, name='login_doctor'),
    path('details/<int:id>/', doctor_details, name='doctor_details'),
    path('reserve/<int:id>/<int:ins_type>/', reserve, name='reserve'),
    path('check_reserve/<int:visit_id>/', check_reserve, name='check_reserve'),
    path('request/', send_request, name='request'),
    path('verify/', verify , name='verify'),
    path('comment/<int:dr_id>/', comment_user, name='comment'),
    path('search/', dr_search, name='dr_search'),
    path('all_doctors/', all_doctors, name='all_doctors'),
]