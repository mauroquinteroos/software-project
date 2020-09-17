from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('rutas/', views.home_routes),
]