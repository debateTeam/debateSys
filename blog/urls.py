from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^login\.html$', views.login, name='login'),
    url(r'index',views.news, name="news"),
    url(r'^contact$', views.contact,name ='contact'),
    url(r'^addUser$', views.addUser,name ='addUser'),
    url(r'^loginCertifacate$', views.loginCertifacate,name ='loginCertifacate'),
    url(r'^addUserView$', views.addUserView,name ='addUserView'),
    url(r'^changePasswd$', views.changePasswd,name ='changePasswd'),
    url(r'^logout$', views.logout,name ='logout'),
 
    url(r'^news/(?P<method>\w+)/(?P<Oid>\w*)$', views.news,name ='news'),
    url(r'^product/(?P<method>\w+)/(?P<Oid>\w*)$', views.product,name ='product'),
    url(r'^plan/(?P<method>\w+)/(?P<Oid>\w*)$', views.plan,name ='plan'),
    url(r'^recruit/(?P<method>\w+)/(?P<Oid>\w*)$', views.recruit,name ='recruit'),
    url(r'^contact/(?P<method>\w+)/(?P<Oid>\w*)$', views.contact,name ='contact'),
    url(r'^us/(?P<method>\w+)/(?P<Oid>\w*)$', views.us,name ='us'),

    

    #file operation 
    url(r'^addImage$', views.addImage,name ='addImage'),
    url(r'^addImageInfo$', views.addImageInfo,name ='addImageInfo'),
    url(r'^showImgList$', views.showImgList,name ='showImgList'),
    url(r'^deleteImg/(?P<Oid>\w+)$', views.deleteImg,name ='deleteImg'),
    url(r'^test$', views.test,name ='test'),
)
