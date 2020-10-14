# Django
from django.shortcuts import render,redirect
from django.http import HttpResponse
import json

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
  project = get_project(cod_project)
  rutas = get_rutas_project(cod_project)
  form=Rutaform()
  return render(request, 'rutas.html', {'project': project, 'rutas': rutas, 'form':form})



def crearRuta(request,idproyecto):
  if request.method == 'GET':
      form=Rutaform()
      form = Rutaform(initial={'codpyto':idproyecto})
      contexto={
        'form':form
      }
  else:
    form=Rutaform(request.POST)
    if form.is_valid():
      form.save()
    return redirect('rutanueva', idproyecto = idproyecto)
  return render(request,'rutas.html',contexto)
 
 def editarRuta(request, idproyecto,idruta):
    ruta = Ruta.objects.get(codpyto=idproyecto,codrutapy = idruta)
    if request.method =='GET':
        form = Rutaform(instance = ruta)
        contexto = {
            'form': form
        }
    else:
        form = Rutaform(request.POST, instance = ruta )
        if form.is_valid():
            form.save()
            return redirect('ruta', idproyecto = idproyecto, idruta = idruta)
    return render(request,'rutas.html',contexto)

def tramos_by_ruta(request, cod_ruta):
  tramos = get_tramos_ruta(cod_ruta)
  ruta = get_ruta(cod_ruta)
  form = TramoForm()
  project = get_project(ruta['codPyto_id'])
  return render(request, 'tramos.html', {'tramos': tramos, 'ruta': ruta, 'project': project, 'form': form })


def editarRuta(request, codRutaPy ):
  rutas=rutas.objects.get(codRutaPy=codRutaPy)
  if request.method=='GET':
    form=Rutaform(instance=rutas)
    contexto={
      'form':form
    }
    return render(request,'rutas.html',contexto)

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
