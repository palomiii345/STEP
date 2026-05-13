from django.urls import path
from . import views

urlpatterns = [

    path('', views.bienvenida, name='bienvenida'),

    path('inicio/', views.inicio, name='inicio'),

    path('servicios/', views.servicios, name='servicios'),

    path('clientes/', views.clientes, name='clientes'),

    path('contacto/', views.contactos, name='contactos'),

    path('nosotros/', views.nosotros, name='nosotros'),
    

]
