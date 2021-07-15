# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import City, Country
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import json as simplejson


class Consultar(ListView):
    model = Country
    template_name = "registro/persona_list.html"

    def get_context_data(self, **kwargs):
        """
        Get the context for this view.
        We pass the cities in context 
        """
        queryset = kwargs.pop('object_list', self.object_list)
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        cities = City.objects.all()
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
                'cities' : cities
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        return super(Consultar, self).get_context_data(**context)
