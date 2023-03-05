from django.forms import forms
from django.contrib.auth.models import User
from django import forms
from .models import Patient
from home.models import Insurance

insurances = (
    ('taamin ejtemaii', 'تامین اجتماعی'),
    ('salamat', 'سلامت'),
    ('niroo mosalah', 'نیروهای مسلح')
)


class PatientRegisterForm(forms.Form):
    username1 = forms.CharField(max_length=100)
    email1 = forms.EmailField()
    f_name1 = forms.CharField(max_length=50)
    l_name1 = forms.CharField(max_length=100)
    national_code1 = forms.IntegerField()
    phone_number1 = forms.IntegerField()
    insurance_type = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=400, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=400, widget=forms.PasswordInput())

    def clean_username1(self):
        u_name = self.cleaned_data['username1']
        if User.objects.filter(username=u_name).exists():
            raise forms.ValidationError('username tekrari')
        return u_name

    def clean_email1(self):
        em = self.cleaned_data['email1']
        if User.objects.filter(email=em).exists():
            raise forms.ValidationError('email tekrari')
        return em

    def clean_national_code1(self):
        n_code = self.cleaned_data['national_code1']
        if Patient.objects.filter(national_code=n_code).exists():
            raise forms.ValidationError('code melli qablan sabt shode')
        return n_code

    def clean_phone_number1(self):
        p_number = self.cleaned_data['phone_number1']
        if Patient.objects.filter(phone_number=p_number).exists():
            raise forms.ValidationError('shomare qablan sabt shde')
        return p_number

    def clean_password2(self):
        passw1 = self.cleaned_data['password1']
        passw2 = self.cleaned_data['password2']
        if passw1 != passw2:
            raise forms.ValidationError("passwords not match")
        if len(passw2) < 8:
            raise forms.ValidationError('bishtar az 8 bashad')
        if not any(i.isalpha() for i in passw2):
            raise forms.ValidationError('hade aqal yek harf vared shavad')
        if not any(i.isupper() for i in passw2):
            raise forms.ValidationError('hade aqal yek harfe bozorg vred shavad')
        return passw2


class LoginUserForm(forms.Form):
    username1 = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=400, widget=forms.PasswordInput())
