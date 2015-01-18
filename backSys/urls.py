from django.conf.urls import patterns, url

from backSys import views

urlpatterns = patterns('',
    url(r'^login\.html$', views.login, name='login'),
)
