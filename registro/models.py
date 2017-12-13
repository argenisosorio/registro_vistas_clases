# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    cedula = models.CharField(max_length=8)

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('registro:editar', kwargs={'pk': self.pk})
