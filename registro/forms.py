# -*- coding: utf-8 -*-
from django import forms
from registro.models import *
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput, DateTimeField
)
from datetime import *


class PersonaForm(forms.ModelForm):
    """
    Formulario que gestiona los campos de un producto.
    """
    nombre = forms.CharField(label='Nombre', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    cedula = forms.CharField(label='Cédula', widget=TextInput(attrs={
        'class':'form-control input-md form_style',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    class Meta:
        model = Persona
        fields = '__all__'