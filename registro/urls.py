# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from registro import views


urlpatterns = patterns('',
    url(r'^$', views.List_files.as_view(), name='list_files'),
    url(r'^file$', views.file, name='file'),
)
