# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Direccion(models.Model):
    nombre_direccion = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre_direccion


class Director(models.Model):
    nombre_director = models.CharField(max_length=250)
    direccion_perteneciente = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre_director


class Proyecto(models.Model):
    """
    Clase que gestiona el modelo de datos de las Personas.
    """
    nombre_proyecto = models.CharField(max_length=250)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre_proyecto

    def get_absolute_url(self):
        return reverse('registro:editar', kwargs={'pk': self.pk})
