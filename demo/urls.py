from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^hello/?$', views.index),
    url(r'^hello/(?P<name>\w+)/?$', views.index),

    url(r'^contact/?$', views.contact),
]
