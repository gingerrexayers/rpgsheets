from __future__ import unicode_literals
from django.db import models
from ..loginreg.models import User

# Create your models here.

class Character(models.model):
    user = models.ForeignKey(User, related_name='characters')
    name = models.CharField(max_length=255)
    alignment = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    char_class = models.CharField(max_length=255)
    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)
	curr_hp = models.IntegerField()
    max_hp = models.IntegerField()
    damage = models.IntegerField()
    armor = models.IntegerField()
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    gear = models.ManyToManyField(Item)

class Item(models.Model):
	name = models.CharField(max_length=255)
	itemType = models.CharField(max_length=255)
	rarity = models.CharField(max_length=255)
	value = models.IntegerField()
