# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import Persona
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import csv


class Consultar(ListView):
    model = Persona


class Registrar(CreateView):
    model = Persona
    fields = ['nombre', 'cedula']
    success_url = reverse_lazy('registro:consultar')


class Editar(UpdateView):
    model = Persona
    fields = ['nombre', 'cedula']
    success_url = reverse_lazy('registro:consultar')


class Borrar(DeleteView):
    model = Persona
    success_url = reverse_lazy('registro:consultar')


def subir_csv(request):
    """
    Función que permite subir el fichero CSV en la carpeta media.
    """
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        file = fs.url(filename)
        return render(request, 'registro/subir_csv.html', {
            'file': file
        })
    return render(request, 'registro/subir_csv.html')


def insertar_data_csv(request, template_name='registro/leer_csv.html'):
    """
    Función que permite insertar los datos del fichero CSV en la base de datos.
    """
    with open(settings.MEDIA_ROOT+'/data.csv', 'r') as listado:
        datos = csv.reader(listado, delimiter=',') # Separar la data por coma.
        for row in datos:
            nombre = row[0]
            cedula = row[1]
            #print "----"
            #print nombre
            #print cedula
            Persona.objects.create(nombre=nombre, cedula=cedula)
    listado.close()
    return render(request, template_name)
