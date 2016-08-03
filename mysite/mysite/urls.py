"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin, staticfiles
from django.conf.urls.static import static
from django import conf

from . import views
from . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'index'),
    url(r'^login', views.Login, name = 'login'),
    url(r'^register', views.register, name = 'register'),
    url(r'^logout', views.Logout, name = 'logout'),
    url(r'^clubs/', include('clubs.urls')),
    url(r'^classes/', include('classes.urls')),
    url(r'^figures/', include('figures.urls')),
    url(r'^forget_password', views.forget_password, name = 'forget_password'),
    url(r'^explain', views.explain, name = 'explain'),
    url(r'^myapp', include('myapp.urls')),
] + static(conf.settings.STATIC_URL, document_root=conf.settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', staticfiles.views.serve),
    ]