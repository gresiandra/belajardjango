from django.conf.urls import url
from django.views.generic.base import TemplateView

from .import views

urlpatterns = [

    #Beberapa cara memanggil template halaman menggunakan ClassBasedView

    #cara pertama : memakai class View saja
    url(r'^$', views.IndexClass.as_view(), name='index'),

    #cara kedua : memakai class TemplateView yang di deklarasikan di view.py
    url(r'^index1$', views.IndexClass2.as_view(template_name='classBased/classBased1.html'), name='index1'),

    #cara ketiga : langsung pakai class TemplateView di urls.py (statis)
    url(r'^index2$', TemplateView.as_view(template_name='classBased/classBased2.html'), name='index2'),

    #cara keempat : mengambil context pada TemplateView (lihat di views.py)
    url(r'^indexContext$', views.IndexContext.as_view(), name='indexContext')
]