from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Campaign(models.model):
    name = models.CharField(max_length=255)
    game_master = models.ForeignKey(User, related_name='campaigns')
