# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Estado(models.Model):
    nombre_estado = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre_estado


class Municipio(models.Model):
    nombre_municipio = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre_municipio


class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    estado = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('registro:editar', kwargs={'pk': self.pk})
