from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from registro.models import Persona

class Consultar(ListView):
    model = Persona
    template_name = 'consultar.html'

class Registrar(CreateView):
    model = Persona
    fields = ['nombre', 'cedula']
    template_name = 'registro/registrar.html'
    success_url = reverse_lazy('registro:consultar')

class Editar(UpdateView):
    model = Persona
    fields = ['nombre', 'cedula']
    success_url = reverse_lazy('registro:consultar')

class Borrar(DeleteView):
    model = Persona
    template_name = 'registro/borrar.html'
    success_url = reverse_lazy('registro:consultar')