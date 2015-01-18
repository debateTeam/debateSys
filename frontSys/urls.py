from django.conf.urls import patterns, url

from frontSys import views

urlpatterns = patterns('',
    url(r'^index\.html$', views.Index, name = "Index"),
    url(r'^member\.html$', views.Member, name = "member"),
    url(r'^article\.html$', views.Article, name = "article"),
    url(r'^register\.html$', views.Register, name = "register"),
)
