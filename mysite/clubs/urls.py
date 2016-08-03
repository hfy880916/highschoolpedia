from django.conf.urls import url
from django.contrib.staticfiles.urls import static

from . import views
from mysite import settings

app_name = 'clubs'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<article_id>[0-9]+)/$', views.article, name = 'article'),
    url(r'^create', views.create, name = 'create'),
    url(r'^(?P<article_id>[0-9]+)/edit', views.edit, name = 'edit'),
    url(r'^(?P<article_id>[0-9]+)/delete', views.delete, name = 'delete'),
    url(r'^(?P<article_id>[0-9]+)/edit', views.img_delete, name = 'img_delete'),
]


