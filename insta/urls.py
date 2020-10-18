from django.conf.urls import url
from .import views


urlpatterns = [
    url('^$', views.index, name='indexpage'),
     url(r'^profile/',views.profile,name ='profile'),
    url(r'^user/(\d+)$', views.profile, name='profile'),
     url(r'^viewprofile/(?P<id>\d+)',views.view_profile,name = 'viewprofile'),
    url(r'^image/$', views.add_new_image, name='upload_image'),
    url(r'^search/$', views.search_user, name='search_profile'),
]