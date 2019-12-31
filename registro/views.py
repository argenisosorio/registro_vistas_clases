# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import Direccion, Director, Proyecto
from registro.forms import ProyectoForm, ProyectoUpdateForm


class Consultar(ListView):
    model = Proyecto


class Registrar(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    success_url = reverse_lazy('registro:consultar')

    def get_context_data(self, **kwargs):
        consulta_direcciones = Direccion.objects.all()
        consulta_directores = Director.objects.all()
        context = {
            'direcciones' : consulta_direcciones,
            'directores' : consulta_directores,
        }
        if self.object:
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super(Registrar, self).get_context_data(**context)


class Editar(UpdateView):
    model = Proyecto
    #form_class = ProyectoUpdateForm
    form_class = ProyectoForm
    template_name = "registro/proyecto_form_update.html"
    success_url = reverse_lazy('registro:consultar')

    def get_context_data(self, **kwargs):
        consulta_direcciones = Direccion.objects.all()
        consulta_directores = Director.objects.all()
        context = {
            'direcciones' : consulta_direcciones,
            'directores' : consulta_directores,
        }
        if self.object:
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super(Editar, self).get_context_data(**context)


class Borrar(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('registro:consultar')
