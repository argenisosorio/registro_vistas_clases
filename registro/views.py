# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import Persona
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class Consultar(ListView):
    model = Persona


class Registrar(SuccessMessageMixin,CreateView):
    model = Persona
    fields = ['nombre', 'cedula']
    success_url = reverse_lazy('registro:consultar')
    success_message = "Se agrego una persona con éxito"


class Editar(SuccessMessageMixin,UpdateView):
    model = Persona
    fields = ['nombre', 'cedula']
    success_url = reverse_lazy('registro:consultar')
    success_message = "Se actualizo una persona con éxito"


class Borrar(DeleteView):
    model = Persona
    success_url = reverse_lazy('registro:consultar')
    success_message = "Se elimino una persona con éxito"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Borrar, self).delete(request, *args, **kwargs)
