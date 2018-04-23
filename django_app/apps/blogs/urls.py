from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<num>\d+)/delete$', views.destroy),
    url(r'^(?P<num>\d+)/edit$', views.edit),
    url(r'^(?P<num>\d+)$', views.show),
    url(r'^create$', views.index),
    url(r'^new$', views.newblog),
    url(r'^$', views.index),
]