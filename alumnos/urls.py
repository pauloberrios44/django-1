from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('generos', views.generos, name="generos"),
    path('usuarios', views.usuarios, name="usuarios")
]