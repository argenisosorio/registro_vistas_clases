# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.description
