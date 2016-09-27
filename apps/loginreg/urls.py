from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^loginsuccess$', views.loginsuccess, name='loginsuccess'),
    url(r'^registersuccess$', views.registersuccess, name='registersuccess'),
    url(r'^logout$', views.logout, name='logout')
]
