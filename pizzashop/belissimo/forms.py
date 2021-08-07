from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactU
        fields = ['name', 'email', 'subject', 'message']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
