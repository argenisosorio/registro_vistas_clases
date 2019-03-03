# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import Persona
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext


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
    success_message = "Se actualizo el registro con éxito"

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta editar el reporte no es el autor/creador.
        """
        self.object = self.get_object()
        if request.user.is_superuser:
            return super(Editar, self).get(request, *args, **kwargs)
        else:
            if str(request.user.last_name) == "user_1":
                return super(Editar, self).get(request, *args, **kwargs)
            else:
                messages_alert = ['No tiene permisos para editar este registro']
                print "No tiene permisos"
                return render_to_response("registro/persona_list.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))


class Borrar(DeleteView):
    model = Persona
    success_url = reverse_lazy('registro:consultar')
