# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from registro import views
from registro.views import *
from django.conf import settings


urlpatterns = patterns('',
    url(r'^$', views.Consultar.as_view(), name='consultar'),
    url(r'^registrar$', views.Registrar.as_view(), name='registrar'),
    url(r'^editar/(?P<pk>\d+)$', views.Editar.as_view(), name='editar'),
    url(r'^borrar/(?P<pk>\d+)$', views.Borrar.as_view(), name='borrar'),
    # Definiendo la url que va a servir los documentos.
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^datos$', views.datos, name='datos'),
)
