from django.conf.urls import patterns, url, include

from . import views

app_name = 'myapp'
urlpatterns = [
url(r'^$', views.list , name = 'list'),
]