from django.urls import path
from . import views

urlpatterns = [
    path('', views.proyectos),
    path('reconocimiento/', views.reconocimiento ),
     path('ruta/', views.ruta),
]