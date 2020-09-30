from django.urls import path
from . import views

urlpatterns = [
    path('', views.proyectos),
    path('rutas/<int:cod_project>', views.rutas_by_project),
    path('tramos/<int:cod_ruta>', views.tramos_by_ruta),
]