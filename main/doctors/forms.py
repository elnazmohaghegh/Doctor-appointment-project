from django.forms import forms
from django import forms
from .models import *


class LoginDoctorForm(forms.Form):
    username123 = forms.CharField(max_length=100)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'placeholder':'ramz bezan'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', 'rate')


class SearchForm(forms.Form):
    search = forms.CharField(max_length=200)