from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)', views.info, name='info'),
    url(r'^(?P<id>\d+)/manage$', views.manage, name='manage')
]
