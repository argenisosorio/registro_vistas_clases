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

    class Meta:
        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'class':'form-control input-md',
                'style': 'min-width: 0; width: 50%; display: inline;',
            }),
            'first_name': forms.TextInput(attrs={
                'class':'form-control input-md',
                'style': 'min-width: 0; width: 50%; display: inline;',
            }),
            'last_name': forms.TextInput(attrs={
                'class':'form-control input-md',
                'style': 'min-width: 0; width: 50%; display: inline;',
            }),
            'email': forms.TextInput(attrs={
                'class':'form-control input-md',
                'style': 'min-width: 0; width: 50%; display: inline;',
            }),
            'password1': forms.TextInput(attrs={
                'class':'form-control input-md',
                'style': 'min-width: 0; width: 50%; display: inline;',
            }),
            'password2': forms.TextInput(attrs={
                'class':'form-control input-md',
                'style': 'min-width: 0; width: 50%; display: inline;',
            }),
        }
