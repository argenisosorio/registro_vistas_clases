# -*- coding: utf-8 -*-
from django import forms
from registro.models import Estado, Municipio, Persona
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput, DateTimeField
)
from datetime import *
from django.contrib.admin.widgets import AdminDateWidget


class PersonaForm(forms.ModelForm):
    """
    Formulario con los campos de una Persona.
    """
    class Meta:

        model = Persona
        fields = '__all__'
