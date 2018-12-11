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

    """
    def __init__(self, *args, **kwargs):
        #
        #Método que carga la data de los Estados y Municipios registrados
        #en el campo estado y municipio de una Persona
        #
        super(PersonaForm, self).__init__(*args, **kwargs)
        lista_estados = Estado.objects.all().values_list('nombre_estado','nombre_estado')
        lista_municipios = Municipio.objects.all().values_list('nombre_municipio','nombre_municipio')

        self.fields['estado'] = forms.ChoiceField(label="Estado", widget=Select(attrs={
            'class':'form-control input-md seleccion',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_estados)

        self.fields['municipio'] = forms.ChoiceField(label="Municipio", widget=Select(attrs={
            'class':'form-control input-md seleccion',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_municipios)
    """

    nombre = forms.CharField(label='Nombre', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    estado = forms.CharField(label='Estado', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    municipio = forms.CharField(label='Municipio', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)
 
    class Meta:

        model = Persona
        fields = '__all__'
