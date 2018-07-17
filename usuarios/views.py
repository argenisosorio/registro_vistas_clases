# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, RedirectView, CreateView, UpdateView, ListView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import forms, login, logout, authenticate
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class LoginView(FormView):
    """
    Clase que gestiona el formulario de inicio de sesión.
    """
    template_name = 'usuarios/login.html'
    form_class = LoginForm

    def get_success_url(self):
        """
        Método que redirecciona al usuario cuando se inicio sesión correctamente.
        """
        return reverse_lazy('registro:consultar')

    def form_valid(self, form):
        """
        Método gestiona la validación de los datos enviados en el formulario.
        """
        usuario = form.cleaned_data['username']
        contrasena = form.cleaned_data['password']
        usuario = authenticate(username=usuario, password=contrasena)
        login(self.request, usuario)
        return super(LoginView, self).form_valid(form)


class RegisterUser(CreateView):
    """
    Clase que gestiona el formulario registro de usuarios.
    """
    model = User
    template_name = "usuarios/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('registro:consultar')
    success_message = "Se registró con éxito"

    def form_valid(self, form):
        """
        Método gestiona la validación de los datos enviados en el
        formulario y envía un mensaje de confirmación.
        """
        self.object = form.save()
        messages.success(self.request, self.success_message)
        return super(RegisterUser, self).form_valid(form)


class Logout(View):
    """
    Clase que gestiona el cierre de sesión.
    """

    def get(self, request):
        """
        Método que gestiona el acceso por get a la clase.
        """
        logout(request)
        return redirect('usuarios:login')
