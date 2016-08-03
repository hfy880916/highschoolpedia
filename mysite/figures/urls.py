from django.conf.urls import url

from . import views

app_name = 'figures'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<article_id>[0-9]+)/$', views.article, name = 'article'),
    url(r'^create', views.create, name = 'create'),
    url(r'^(?P<article_id>[0-9]+)/edit', views.edit, name = 'edit'),
    url(r'^(?P<article_id>[0-9]+)/delete', views.delete, name = 'delete'),
]