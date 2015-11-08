"""chorelist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$',  views.index, name='index'),
    url(r'^newlist/$',  views.newlist, name='newlist'),

    url(r'^(?P<chorelist_id>[0-9]+)/$',  views.detail, name='detail'),
    # url(r'^(?P<chorelist_id>[0-9]+)/chores/$',  views.chores, name='chores'),
    url(r'^(?P<chorelist_id>[0-9]+)/chores/(?P<chore_id>[0-9]+)/$',  views.choredetail, name='choredetail'),
    url(r'^(?P<chorelist_id>[0-9]+)/chores/(?P<chore_id>[0-9]+)/update/$',  views.updatechore, name='updatechore')

]
