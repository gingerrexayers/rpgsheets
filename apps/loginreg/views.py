from django.shortcuts import render, redirect
from .models import User
from django.core.urlresolvers import reverse
from django.contrib import messages
import datetime
# Create your views here.

def index(request):
    context = {
        'today': str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d'))
    }
    return render(request, 'loginreg/index.html', context)

def register(request):
    if request.method=='POST':
        result = User.manager.register(request.POST)

        if result[0]:
            request.session['id'] = result[1].id
            return redirect(reverse('login:registersuccess'))
        else:
            for e in result[1]:
                messages.error(request, e)
            return redirect(reverse('login:index'))

def login(request):
    if request.method=='POST':
        result = User.manager.login(request.POST)
        if result[0]:
            request.session['id'] = result[1].id
            return redirect(reverse('login:loginsuccess'))
        else:
            for e in i[1]:
                messages.error(request, e)
            return redirect(reverse('login:index'))

def logout(request):
    request.session.pop('id')
    return redirect(reverse('login:index'))

def loginsuccess(request):
    return redirect(reverse('wishlist:index'))

def registersuccess(request):
    return redirect(reverse('wishlist:userinit'))
