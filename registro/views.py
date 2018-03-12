# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import Document
from registro.forms import DocumentForm
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect


def file(request):
    """
    Función que permite guardar los documentos, se guardar en /media
    """
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('registro:list_files')
    else:
        form = DocumentForm()
    return render(request, 'registro/file.html', {
        'form': form
    })


class List_files(ListView):
    """
    Clase que permite listar los documentos registrados
    """
    model = Document
    template_name = "registro/list_files.html"
