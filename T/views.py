# Django
from django.shortcuts import render

# Models
from T.models import *


# Consultas
def get_projects():
  proyecto = Proyecto.objects.all()
  return proyecto

def get_project(codProject):
  project = Proyecto.objects.get(codPyto=codProject)
  return project

def get_rutas_project(codProject):
  rutas = Ruta.objects.filter(codPyto=codProject)
  return rutas

def get_ruta(codRuta):
  ruta = Ruta.objects.filter(codRutaPy=codRuta).values()
  return ruta[0]

def get_tramos_ruta(codRuta):
  tramos = Tramo.objects.filter(codRutaPy=codRuta)
  return tramos

def get_tramo(codTramo):
  tramo = Tramo.objects.get(codTramoPy=codTramo)
  return tramo


# Controller
def proyectos(request):
  projects = get_projects()
  return render(request, 'proyecto.html', {'projects': projects})

def rutas_by_project(request, cod_project):
  project = get_project(cod_project)
  rutas = get_rutas_project(cod_project)
  return render(request, 'rutas.html', {'project': project, 'rutas': rutas})

def tramos_by_ruta(request, cod_ruta):
  tramos = get_tramos_ruta(cod_ruta)
  ruta = get_ruta(cod_ruta)
  project = get_project(ruta['codPyto_id'])
  return render(request, 'tramos.html', {'tramos': tramos, 'ruta': ruta, 'project': project})
