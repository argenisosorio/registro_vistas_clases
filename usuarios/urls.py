# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from usuarios import views
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'^$', LoginView.as_view(), name = "login"),
    url(r'^register$', views.RegisterUser.as_view(), name='register'),
    url(r'logout/$', views.Logout.as_view(), name='logout'),
    url(r'^list_users/$', login_required(views.ListUsers.as_view()), name='list_users'),
)
