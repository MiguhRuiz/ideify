from __future__ import unicode_literals

from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=1000)
    image_URL = models.CharField(max_length=2500)

    def __str__(self):
        return self.name
