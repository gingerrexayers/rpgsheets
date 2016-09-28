from __future__ import unicode_literals
from ..loginreg.models import User
from django.db import models

# Create your models here.
class Campaign(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    game_master = models.ForeignKey(User, related_name='campaigns')
    players = models.ManyToManyField(User, related_name='active_games')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)