from django.urls import path
from . import views

urlpatterns = [
    path('', views.ruta),
    path('reconocimiento/', views.reconocimiento ),
]