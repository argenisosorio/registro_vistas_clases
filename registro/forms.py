# -*- coding: utf-8 -*-
from django import forms
from registro.models import Direccion, Director, Proyecto
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput, DateTimeField
)
from datetime import *
from django.contrib.admin.widgets import AdminDateWidget


class ProyectoForm(forms.ModelForm):

    class Meta:
        model = Proyecto
        fields = '__all__'


class ProyectoUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProyectoUpdateForm, self).__init__(*args, **kwargs)
        lista_direcciones = Direccion.objects.all().values_list('nombre_direccion','nombre_direccion')
        lista_directores = Director.objects.all().values_list('nombre_director','nombre_director')
        self.fields['direccion'] = forms.ChoiceField(label="Dirección", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_direcciones)

        self.fields['director'] = forms.ChoiceField(label="Director", widget=Select(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
        }), choices=lista_directores)

    nombre_proyecto = forms.CharField(label='Nombre del proyecto', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 50%; display: inline;',
        'value': '0',
    }), required = True)

    class Meta:
        model = Proyecto
        fields = '__all__'
