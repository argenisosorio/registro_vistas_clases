# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User, UserManager, Permission
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms import (
    ModelForm, TextInput, EmailInput, CharField, EmailField, PasswordInput, Select
)
from django import forms


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }), required = True)

    password = forms.CharField(widget=PasswordInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }), required = True)

    class Meta:
        model = User

    fields = [
        'username',
        'password',
    ]


class MyRegistrationForm(UserCreationForm):
    """
    #Clase del formulario que registra los usuarios
    """
    username = forms.CharField(required = True)
    class Meta:
        model = User
        fields = ('username','password1','password2','first_name','last_name','email','is_staff','is_active')
