# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from registro import views


urlpatterns = patterns('',
    url(r'^$', views.Consultar.as_view(), name='consultar'),
)
