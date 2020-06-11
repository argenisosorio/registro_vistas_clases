# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import Persona
from registro.forms import PersonaForm
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect


class Consultar(ListView):
    model = Persona

    def get_context_data(self, **kwargs):
        queryset = kwargs.pop('object_list', self.object_list)
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        form = PersonaForm()
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context = {
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'object_list': queryset,
            }
        else:
            context = {
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset,
                'form':form,
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        return super(Consultar, self).get_context_data(**context)


class Registrar(CreateView):
    model = Persona
    form_class = PersonaForm
    success_url = reverse_lazy('registro:consultar')

    def get_context_data(self, **kwargs):
        queryset = Persona.objects.all()
        context = {
            'object_list': queryset,
        }
        if self.object:
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super(Registrar, self).get_context_data(**context)


class Editar(UpdateView):
    template_name = "registro/persona_form_update.html"
    model = Persona
    form_class = PersonaForm
    success_url = reverse_lazy('registro:consultar')

    def get_context_data(self, **kwargs):
        queryset = Persona.objects.all()
        context = {
            'object_list': queryset,
        }
        if self.object:
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super(Editar, self).get_context_data(**context)


class Borrar(DeleteView):
    model = Persona
    success_url = reverse_lazy('registro:consultar')
