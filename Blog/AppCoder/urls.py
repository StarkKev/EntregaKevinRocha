from django.urls import path
from AppCoder import views

urlpatterns= [
    path("",views.inicio,name='inicio'),
    path("videojuegos/", views.videojuegos,name='videojuegos'),
    path("hardware/", views.hardware,name='hardware'),
    path("plataformas/", views.plataformas,name='plataformas'),
    path("buscarvideojuegos/", views.buscar),
    path("busquedaVideojuegos/", views.buscarvideojuegos),
    path("buscarhardware/", views.buscar2),
    path("busquedaHardware/", views.buscarhardware),
    path("buscarplataforma/", views.buscar3),
    path("busquedaPlataforma/", views.buscarplataforma),
]