# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from datetime import datetime
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.auth.models import User
from registro.models import Persona, Bitacora


class Consultar(ListView):
    """
    Clase que muestra la lista de personas registradas
    """
    model = Persona

    def get(self, request, *args, **kwargs):
        """
        Método que muestra cual usuario y cuando visito la lista de personas.
        """
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        context = self.get_context_data(object_list=self.object_list)
        #print "***** El usuario: "+str(self.request.user)+", visito la lista de personas el: "+str(datetime.now())+" *****"
        #a = "El usuario: "+str(self.request.user)+", visito la lista de personas el: "+str(datetime.now())
        #Bitacora.objects.create(entrada=a)
        return self.render_to_response(context)


class Registrar(CreateView):
    """
    Clase que permite registrar personas
    """
    model = Persona
    fields = ['nombre', 'cedula']
    success_url = reverse_lazy('registro:consultar')

    def form_valid(self, form):
        """
        Método que muestra cual usuario y cuando registro a una persona y lo guara en la tabla bitacora
        """
        self.object = form.save()
        #print "***** El usuario: "+str(self.request.user)+", registro una persona el: "+str(datetime.now())+" *****"
        a = "El usuario: "+str(self.request.user)+", registro una persona el: "+str(datetime.now())
        Bitacora.objects.create(entrada=a)
        return super(Registrar, self).form_valid(form)


class Editar(UpdateView):
    """
    Clase que permite editar a las personas
    """
    model = Persona
    fields = ['nombre', 'cedula']
    success_url = reverse_lazy('registro:consultar')

    def form_valid(self, form):
        """
        Método que muestra cual usuario y cuando actualizo a una persona y lo guara en la tabla bitacora
        """
        self.object = form.save()
        #print "***** El usuario: "+str(self.request.user)+", actualizo una persona el: "+str(datetime.now())+" *****"
        a = "El usuario: "+str(self.request.user)+", actualizó una persona el: "+str(datetime.now())
        Bitacora.objects.create(entrada=a)
        return super(Editar, self).form_valid(form)


class Borrar(DeleteView):
    """
    Clase que permite eliminar una persona
    """
    model = Persona
    success_url = reverse_lazy('registro:consultar')

    def delete(self, request, *args, **kwargs):
        """
        Método que muestra cual usuario y cuando elimino a una persona y lo guara en la tabla bitacora
        """
        #print "***** El usuario: "+str(self.request.user)+", elimino a una persona el: "+str(datetime.now())+" *****"
        a = "El usuario: "+str(self.request.user)+", elimino una persona el: "+str(datetime.now())
        Bitacora.objects.create(entrada=a)
        return super(Borrar, self).delete(self, request, *args, **kwargs)


class BitacoraView(ListView):
    """
    Clase que muestra la lista de entradas de la bitácora
    """
    model = Bitacora
    template_name = "registro/bitacora.html"
