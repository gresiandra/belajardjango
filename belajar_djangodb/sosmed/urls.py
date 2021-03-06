from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^delete/(?P<delete_id>[1-9]|[1-9][0-9]|[1-9][0-9][0-9])$', views.delete, name='delete'),
    url(r'^update/(?P<update_id>[1-9]|[1-9][0-9]|[1-9][0-9][0-9])$', views.update, name='update'),
]