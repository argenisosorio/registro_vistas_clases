# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, RedirectView, CreateView, UpdateView, ListView, TemplateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import forms, login, logout, authenticate
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import LoginForm, MyRegistrationForm, UserForm
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
    form_class = MyRegistrationForm
    success_url = reverse_lazy('usuarios:list_users')
    success_message = "Se registró con éxito"

    def form_valid(self, form):
        """
        Método gestiona la validación de los datos enviados en el
        formulario y envía un mensaje de confirmación.
        """
        self.object = form.save(commit=False)
        self.object.username = form.cleaned_data['username']
        self.object.first_name = form.cleaned_data['first_name']
        self.object.last_name = form.cleaned_data['last_name']
        self.object.password1 = form.cleaned_data['password1']
        self.object.password2 = form.cleaned_data['password2']
        #self.object.is_staff = form.cleaned_data['is_staff']
        #self.object.is_active = form.cleaned_data['is_active']
        self.object.is_active = 1
        self.object.is_staff = 0
        self.object.save()
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


class ListUsers(ListView):
    """
    Clase que permite consultar la lista de usuarios.
    """
    model = User
    template_name = "usuarios/list_users.html"


class EditUser(SuccessMessageMixin, UpdateView):
    """
    Clase que gestiona la actualización de los datos de un usuario del sistema.
    """
    model = User
    template_name = "usuarios/edit_user.html"
    form_class = UserForm
    success_message = "¡Usuario actualizado!"
    success_url = reverse_lazy('usuarios:list_users')


class DeleteUser(SuccessMessageMixin, DeleteView):
    """
    Clase que permite borrar un usuario del sistema.
    """
    model = User
    success_url = reverse_lazy('usuarios:list_users')
    template_name = "usuarios/user_confirm_delete.html"
    success_message = "Se elimino el usuario con éxito"

    def delete(self, request, *args, **kwargs):
        """
        Método que envía el mensaje a la plantilla cuando se
        borra un usuario del sistema.
        """
        messages.success(self.request, self.success_message)
        return super(DeleteUser, self).delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Método que redirecciona a index si el usuario
        que intenta borrar el usuario del sistema no está activo.
        """
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        self.object = self.get_object()
        if request.user.is_active:
            return self.render_to_response(context)
        else:
            if str(self.object) == str(self.request.user):
                return self.render_to_response(context)
            else:
                messages_alert = ['No tiene permisos para borrar el usuario del sistema']
                return render_to_response("inicio/index.html",{'messages_alert': messages_alert}, context_instance=RequestContext(request))