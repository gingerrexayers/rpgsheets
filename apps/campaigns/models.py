from __future__ import unicode_literals
from ..loginreg.models import User
from django.db import models

# Create your models here.
class CampaignManager(models.Manager):
    def add_player(self, campaign_id, form_data):
        u = User.manager.get(id=form_data['user'])
        c = self.get(id=campaign_id)
        c.players.add(u)
        return True
    def update_info(self, campaign_id, form_data):
        errors = []
        if not form_data['name']:
            errors.append('Name cannot be empty!')
        if not form_data['description']:
            errors.append('Description cannot be empty!')
        if errors:
            return (False, errors)

        c = self.get(id=campaign_id)
        c.name = form_data['name']
        c.description = form_data['description']
        c.save()
        return (True, ['Campaign updated successfully!'])

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    game_master = models.ForeignKey(User, related_name='campaigns')
    players = models.ManyToManyField(User, related_name='active_games')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
