from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Character(models.model):
    user = models.ForeignKey(User, related_name='characters')
    name = models.CharField(max_length=255)
