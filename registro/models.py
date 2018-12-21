# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Estado(models.Model):
    """
    Clase que gestiona el modelo de datos de los Estados.
    """
    nombre_estado = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre_estado


class Municipio(models.Model):
    """
    Clase que gestiona el modelo de datos de los Municipios.
    """
    nombre_municipio = models.CharField(max_length=250)
    estado_perteneciente = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre_municipio


class Parroquia(models.Model):
    """
    Clase que gestiona el modelo de datos de las Parroquias.
    """
    nombre_parroquia = models.CharField(max_length=250)
    municipio_perteneciente = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre_parroquia


class Persona(models.Model):
    """
    Clase que gestiona el modelo de datos de las Personas.
    """
    nombre_persona = models.CharField(max_length=250)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre_persona

    def get_absolute_url(self):
        return reverse('registro:editar', kwargs={'pk': self.pk})
