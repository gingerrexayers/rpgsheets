from __future__ import unicode_literals
from django.db import models
import bcrypt, datetime
# Create your models here.
class UserManager(models.Manager):
    def register(self, form_data):
        errors = []
        if len(form_data['name']) < 3:
            errors.append('Name must be at least three characters!')
        if len(form_data['username']) < 3:
            errors.append('Username must be at least three characters!')
        if not all(x.isalpha() or x.isspace() for x in form_data['name']):
            errors.append('Name must be alphabetic!')
        if not form_data['username']:
            errors.append('Username is required!')
        if len(form_data['password']) < 8:
            errors.append('Password must be at least eight characters!')
        if form_data['password'] != form_data['confirmation']:
            errors.append('Password and confirmation must match!')
        if self.filter(username=form_data['username']):
            errors.append('Username is taken!')
        if errors:
            return (False, errors)

        u = self.create(name=form_data['name'], username=form_data['username'], password=bcrypt.hashpw(form_data['password'].encode('utf-8'), bcrypt.gensalt()))
        return (True, u)

    def login(self, form_data):
        errors = []
        if not form_data['username']:
            errors.append('Please enter your username!')
            return (False, errors)
        u = self.filter(username=form_data['username'])[:1]
        if not u:
            errors.append('Invalid username or password')
            return (False, errors)
        if not bcrypt.hashpw(form_data['password'].encode('utf-8'), u[0].password.encode('utf-8')) == u[0].password:
            errors.append('Invalid username or password')
            return (False, errors)
        else:
            return (True, u[0])

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    manager = UserManager()
