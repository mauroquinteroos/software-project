# Django
from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from .models import Ruta

# Models
from T.models import *

from .forms import *

# Consultas
def get_projects():
  proyecto = Proyecto.objects.all()
  print(proyecto)
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
  if request.method == 'GET':
    project = get_project(cod_project)
    rutas = get_rutas_project(cod_project)
    form=Rutaform()
    form= Rutaform(initial={
      'codPyto':cod_project
    })
    contexto = {'project': project, 'rutas': rutas, 'form':form}
  else :
    form=Rutaform(request.POST)
    print('no entro')
    if form.is_valid():
      form.save()
    return redirect('ruta', cod_project = cod_project)
  return render(request, 'rutas.html', contexto)

def editarRuta(request, codRutaPy):
    ruta = Ruta.objects.get(codRutaPy = codRutaPy)
    if request.method =='GET':
        form = Rutaform(instance = ruta)
        contexto = {
            'form': form
        }
    else:
        form = Rutaform(request.POST, instance = ruta )
        if form.is_valid():
            form.save()
            return redirect('ruta',codRutaPy = codRutaPy)
    return render(request,'rutas.html',contexto) 

def tramos_by_ruta(request, cod_ruta):
  if request.method == 'GET':
    tramos = get_tramos_ruta(cod_ruta)
    ruta = get_ruta(cod_ruta)
    project = get_project(ruta['codPyto_id'])
    form = TramoForm()
    form = TramoForm(initial={
      'codPyto':ruta['codPyto_id'],
      'codRutaPy':cod_ruta
    })
    contexto = {'tramos': tramos, 'ruta': ruta, 'project': project, 'form': form }
  else:
    form=TramoForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('tramo',cod_ruta = cod_ruta)
  return render(request, 'tramos.html', contexto)


def json_ruta(request, cod_ruta):
  ruta = get_ruta(cod_ruta)
  print(ruta)
  rutajson={
    'nombre':ruta['codRutaPy'],
    'denominacion':ruta['denominacionRuta']
  }
  return HttpResponse(
    json.dumps(rutajson),
    
    content_type='application/json'
  )
