from django.urls import path
from .views import *

app_name = 'patients'

urlpatterns = [
    path('signup/', p_signup, name='p_signup'),
    path('login/', p_login, name='p_login'),
    path('profile/', user_profile, name='profile'),
    path('reserved_visits/', reserved_visits, name='reserved_visits'),
    path('logout/', user_logout, name='logout')
]