# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import Persona
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import json
from django.core import *


def datos(request):
    result=Persona.objects.values('nombre','cedula').all();
    result=list(result)  #after getting data from model convert result to list
    #print result
    for item in result:
        #print "-----"
        #print item
        items = {}
        items['obj'] = item
    print "----"
    print items
    #c = {"nombre":"John","cedula":"18902230"}
    #return HttpResponse(json.dumps(c), content_type = "application/json")
    return HttpResponse(json.dumps(items), content_type = "application/json")


class Consultar(ListView):
    model = Persona

    def get_context_data(self, **kwargs):
        """
        Get the context for this view.
        """
        queryset = kwargs.pop('object_list', self.object_list)
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context = {
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'object_list': queryset
            }
        else:
            context = {
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset,
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        return super(Consultar, self).get_context_data(**context)


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
