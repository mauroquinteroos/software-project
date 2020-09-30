from django.shortcuts import render
from django.http import HttpResponse
from T.models import *
from datetime import datetime

import json

# Llamar Templates
def ruta(request):
  # proyecto = obtener_proyecto()
  # return render(request, 'rutas.html', {'proyecto': empleado})
  return render(request, 'rutas.html')

def reconocimiento(request):
  return render(request, 'reconocimiento.html')

def proyectos(request):
  return render(request, 'proyecto.html')
# Realizar consultas
def get_empleado(): # Funcion de prueba, eliminarlo despues
  empleado = Empleado.objects.get(dni = '77382771')
  return empleado

def obtener_proyecto():
  proyecto = Proyecto.objects.get(codpyto = 1) # cambiar codigo segun la bd
  return proyecto

def obtener_rutas():
  rutas = Ruta.objects.all()
  return rutas

def obtener_tramos():
  tramos = Tramo.objects.all()
  return tramos