# Django
from django.shortcuts import render

# Models
from T.models import *

# Consultas
def get_projects():
  proyecto = Proyecto.objects.all()
  return proyecto

def get_rutas_project(codProject):
  rutas = Ruta.objects.filter(codPyto=codProject)
  return rutas

def get_ruta(codRuta):
  ruta = Ruta.object.get(codRutaPy=codRuta)
  return ruta

def get_tramos_ruta(codRuta):
  tramos = Tramo.objects.filter(codRutaPy=codRuta)
  return tramos

def get_tramo(codTramo):
  tramo = Tramo.objects.get(codTramoPy=codTramo)
  return tramo

# prueba
projects = [
  {
    'id': 123,
    'rutas': 'message 1'
  },
  {
    'id': 245,
    'rutas': 'message 2'
  },
  {
    'id': 567,
    'rutas': 'message 3'
  },
]

# Controller
def proyectos(request):
  projects = get_projects()
  return render(request, 'proyecto.html', {'projects': projects})


def rutas_by_project(request, cod_project):
  print(cod_project)
  return render(request, 'rutas.html')


def tramos_by_project(request):
  return render(request, 'rutas.html')
