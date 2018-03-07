from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.selector),
    url(r'^(?P<city>[\w\-\s]+)/?$', views.index),
]
