from __future__ import unicode_literals
from django.db import models
from ..loginreg.models import User

# Create your models here.

class Attributes(models.Model):
	char_name = models.ForeignKey(Character)
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

class CharacterJobs(models.Model):
	name = models.CharField(max_length=255)

class CharacterRace(models.Model):
	name = models.CharField(max_length=255)

class CharAlignment(models.Model):
	name = models.CharField(max_length=255)	

class Character(models.model):
    user = models.ForeignKey(User, related_name='characters')
    name = models.CharField(max_length=255)
    alignment = models.ForeignKey(CharAlignment, related_name="characterAlignment")
    race = models.ForeignKey(CharacterRace, related_name="races")
    job = models.ForeignKey(CharacterJobs, related_name="characterJob")
    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)
    gear = models.ForeignKey(Item)

class Item(models.Model):
	name = models.CharField(max_length=255)
	itemType = models.ForeignKey(ItemType)
	rarity = models.CharField(max_length=255)
	value = models.IntegerField()

class Rarity(models.Model):
	name = models.CharField(max_length=255)

class ItemType(models.Model):
	name = models.CharField(max_length=255)

class Weapons(models.Model):
	name = models.CharField(max_length=255)


