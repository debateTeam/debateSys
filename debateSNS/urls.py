#!/usr/bin/python
# coding=utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
from backSys.views import *
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'debateSNS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^blog/',include('blog.urls')),
    url(r'^backSys/',include('backSys.urls')),
    url(r'',include('frontSys.urls'))
)
