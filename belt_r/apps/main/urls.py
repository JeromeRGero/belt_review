from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'reg$', views.reg),
    url(r'logout$', views.logout),
    url(r'login$', views.login),
    url(r'books$', views.books),
    url(r'books/add$', views.addpage),
    # url(r'delete/(?P<num>\d+)$', views.delete),
    url(r'books/add/adding$', views.adding),
    # url(r'^books/(?P<num>\d+)$', views.bookpage),
    # url(r'^user/(?P<num>\d+)$', views.userpage),
    # url(r'^books/submit/(?P<num>\d+)$', views.submitreview),
]
