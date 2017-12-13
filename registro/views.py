# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import Persona, Document
from registro.forms import DocumentForm
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect


def file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('registro:consultar')
    else:
        form = DocumentForm()
    return render(request, 'registro/file.html', {
        'form': form
    })


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
