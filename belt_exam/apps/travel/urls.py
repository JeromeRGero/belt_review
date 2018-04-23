from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'main$', views.index),
    url(r'^travels', views.travelspage),
    url(r'add$', views.addtrippage),
    url(r'travels/destination/(?P<num>\d+)$', views.destinationpage),
    url(r'adding$', views.adding),
    url(r'^main/login$', views.login),
    url(r'^main/reg$', views.reg),
    url(r'logout$', views.logout),
    url(r'$', views.forOfor),
]