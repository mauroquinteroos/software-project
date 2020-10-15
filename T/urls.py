from django.urls import path
from . import views

urlpatterns = [
    path('', views.proyectos),
    path('rutas/<int:cod_project>', views.rutas_by_project, name ='ruta' ),
    # path('editarrutas/<int:codRutaPy>', views.editarRuta, name ='editarRuta' ),
    path('eliminarRuta/<int:codRutaPy>', views.editarRuta, name ='eliminarRuta' ),
    path('tramos/<int:cod_ruta>', views.tramos_by_ruta, name='tramo'),
    path('api/ruta/<int:cod_ruta>', views.json_ruta)
]