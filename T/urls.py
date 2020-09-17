from django.urls import path
from . import views

urlpatterns = [
    path('reconocimiento/', views.reconocimiento ),
]