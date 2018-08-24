# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):
    # Establece la relación entre el usuario de Django y el perfil.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Establece el campo de la cedula del usuario.
    cedula = models.CharField(max_length=50)

    def __unicode__(self):
        return self.cedula
