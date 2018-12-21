# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import Estado, Municipio, Parroquia, Persona
from registro.forms import PersonaForm


class Consultar(ListView):
    """
    Clase que permite consultar la lista de personas registradas.
    """
    model = Persona


class Registrar(CreateView):
    model = Persona
    form_class = PersonaForm
    success_url = reverse_lazy('registro:consultar')

    def get_context_data(self, **kwargs):
        """
        Método que permite pasarle la lista de Estados, Municipios y Parroquias
        registrados.
        """
        consulta_estados = Estado.objects.all()
        consulta_municipios = Municipio.objects.all()
        consulta_parroquias = Parroquia.objects.all()
        context = {
            'estados' : consulta_estados,
            'municipios' : consulta_municipios,
            'parroquias' : consulta_parroquias
        }
        if self.object:
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super(Registrar, self).get_context_data(**context)


class Editar(UpdateView):
    """
    Clase que permite actualizar la data de una persona registrada.
    """
    model = Persona
    form_class = PersonaForm
    template_name = "registro/persona_form_update.html"
    success_url = reverse_lazy('registro:consultar')


class Borrar(DeleteView):
    """
    Método que permite eliminar una persona registrada
    """
    model = Persona
    success_url = reverse_lazy('registro:consultar')
