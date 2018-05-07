# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from registro import views
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'^consultar$', login_required(views.Consultar.as_view()), name='consultar'),
    url(r'^registrar$', login_required(views.Registrar.as_view()), name='registrar'),
    url(r'^editar/(?P<pk>\d+)$', login_required(views.Editar.as_view()), name='editar'),
    url(r'^borrar/(?P<pk>\d+)$', login_required(views.Borrar.as_view()), name='borrar'),
)
