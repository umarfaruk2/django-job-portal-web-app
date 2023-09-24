from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import RegisterInfoModel
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(help_text='')
    email = forms.CharField(label='Email', widget=forms.EmailInput())
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput())

    company = forms.BooleanField(required=False)
    candidate = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('username', 'email', 'password1', 'password2', 'company', 'candidate')
    
    