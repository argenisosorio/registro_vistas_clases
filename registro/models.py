# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name