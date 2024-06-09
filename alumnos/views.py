from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    context = {}
    return render(request, 'alumnos/index.html', context)

def generos(request):
    context = { "generos" : Genero.objects.all() }
    return render(request, 'alumnos/generos.html', context)

def usuarios(request):
    context = { "usuarios": Usuario.objects.select_related('id_genero').all()}
    return render(request, 'alumnos/usuarios.html', context)