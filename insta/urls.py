from django.conf.urls import url
from .import views


urlpatterns = [
    url('^$', views.index, name='indexpage'),
     url(r'^profile/',views.profile,name ='profile'),
    url(r'^user/(\d+)$', views.profile, name='profile'),
]