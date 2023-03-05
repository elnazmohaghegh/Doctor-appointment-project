from django.urls import path
from .views import doctors_list_view

app_name = 'home'


urlpatterns = [
    path('', doctors_list_view, name='doctors_list')
]