from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="tasks-list"),
    url(r'^delete/(\d+)/?$', views.delete, name="tasks-delete"),
    url(r'^toggle/(\d+)/?$', views.toggle, name="tasks-toggle"),
    url(r'^add/?$', views.add, name="tasks-add"),
]
