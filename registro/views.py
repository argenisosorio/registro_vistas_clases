# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import Persona
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def file(request):
    """
    Función que permite guardar los archivos subidos en el servidor.
    """
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        # Ruta donde está almacenado el archivo
        file = fs.url(filename)
        return render(request, 'registro/file.html', {
            'file': file
        })
    # Definimos en el settings la carpeta donde se van a guardar los documentos adjuntos.
    # El archivo será guardado en la carpeta "media" en la raíz del proyecto.
    return render(request, 'registro/file.html')


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
