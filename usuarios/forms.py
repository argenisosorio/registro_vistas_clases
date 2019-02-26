# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User, UserManager, Permission
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.forms import (
    ModelForm, TextInput, EmailInput, CharField, EmailField, PasswordInput, Select, CheckboxInput
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
    username = forms.CharField(label='Nombre de usuario',widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }), required = True)

    password1 = forms.CharField(label='Contraseña',widget=PasswordInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }), required = True)

    password2 = forms.CharField(label='Confirmar contraseña',widget=PasswordInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }), required = True)

    first_name = forms.CharField(label='Primer nombre',widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }), required = True)

    last_name = forms.CharField(label='Primer apellido',widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }), required = True)

    email = forms.EmailField(label='Correo electrónico',widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }), required = True)

    is_active = forms.BooleanField(label='¿Estará activo?',widget=CheckboxInput(attrs={
        #'class':'form-control input-md',
        #'style': 'min-width: 0; width: 25%; display: inline;',
    }), required = False)

    is_staff = forms.BooleanField(label='¿Es staff?',widget=CheckboxInput(attrs={
        #'class':'form-control input-md',
        #'style': 'min-width: 0; width: 25%; display: inline;',
    }), required = False)

    class Meta:
        model = User
        fields = ('username','password1','password2','first_name','last_name','email','is_staff','is_active')


class UserForm(forms.ModelForm):
    """
    #Clase del formulario que registra los usuarios
    """
    username = forms.CharField(label='Nombre de usuario',widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }), required = True)

    first_name = forms.CharField(label='Primer nombre',widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }), required = True)

    last_name = forms.CharField(label='Primer apellido',widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }), required = True)

    email = forms.EmailField(label='Correo electrónico',widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 25%; display: inline;',
    }), required = True)

    is_active = forms.BooleanField(label='¿Está activo?',widget=CheckboxInput(attrs={
    }), required = False)

    is_staff = forms.BooleanField(label='¿Es staff?',widget=CheckboxInput(attrs={
    }), required = False)

    class Meta:
        model = User
        exclude = ('password1','password2')
        fields = ('username','first_name','last_name','email','is_staff','is_active')
