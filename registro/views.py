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


def getdetails(request):

    #country_name = request.POST['country_name']
    country_name = request.GET['cnt']
    #print("ajax " + str(country_name))

    result_set = []
    all_cities = []

    answer = str(country_name[1:-1])
    selected_country = Country.objects.get(name=answer)
    #print("selected country name " + str(selected_country))

    all_cities = selected_country.city_set.all()
    for city in all_cities:
        #print("city name " + str(city.name))
        result_set.append({'name': city.name})

    return HttpResponse(simplejson.dumps(result_set), content_type='application/json')
