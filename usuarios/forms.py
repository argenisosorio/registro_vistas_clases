# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
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


class RegisterForm(UserCreationForm):
    """
    Clase del formulario que registra los usuarios
    """

    username = forms.CharField(max_length=30, label=("Usuario"), widget=forms.TextInput(attrs={
        'class': 'form-control',
        'style': 'min-width: 0; width: 25%; display: inline;',
        'required': 'true',
    }), required = True)

    first_name = forms.CharField(label=("Nombres"), widget=forms.TextInput(attrs={
        'class': 'form-control',
        'style': 'min-width: 0; width: 25%; display: inline;',
        'required': 'true',
    }), required = True)
    
    last_name = forms.CharField(label=("Apellidos"), widget=forms.TextInput(attrs={
        'class': 'form-control',
        'style': 'min-width: 0; width: 25%; display: inline;',
        'required': 'true',
    }), required = True)

    email = forms.CharField(label=("Email"), widget=forms.TextInput(attrs={
        'class': 'form-control',
        'style': 'min-width: 0; width: 25%; display: inline;',
        'required': 'true',
    }), required = True)

    password1 = forms.CharField(label=("Contraseña"), widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'style': 'min-width: 0; width: 25%; display: inline;',
        'required': 'true',
    }), required = True)

    password2 = forms.CharField(label=("Contraseña (confirmación)"), widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'style': 'min-width: 0; width: 25%; display: inline;',
        'required': 'true',
    }), required = True)

    cedula = forms.CharField(label=("Cédula"), widget=forms.TextInput(attrs={
        'class': 'form-control',
        'style': 'min-width: 0; width: 25%; display: inline;',
        'required': 'true',
    }), required = True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name',  'email', 'username', 'password1', 'password2', 'cedula')
