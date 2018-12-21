# -*- coding: utf-8 -*-
from django.contrib import admin
from registro.models import Estado, Municipio, Parroquia, Persona

admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Parroquia)
admin.site.register(Persona)
