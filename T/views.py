from django.shortcuts import render

def ruta(request):
    return render(request, 'rutas.html')

def reconocimiento(request):
    return render(request, 'reconocimiento.html')
