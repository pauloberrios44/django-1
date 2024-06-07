from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    context = {}
    return render(request, 'alumnos/index.html', context)

def generos(request):
    context = { "generos" : Genero.objects.all() }
    return render(request, 'alumnos/generos.html', context)