from django.urls import path
from . import views

urlpatterns = [
    path('', views.proyectos),
    path('rutas/<int:cod_project>', views.rutas_by_project, name ='ruta' ),
    path('editarRuta/<int:cod_project>/<int:cod_ruta>', views.editarRuta, name ='editarRuta' ),
    path('eliminarRuta/<int:cod_project>/<int:cod_ruta>', views.eliminarRuta, name ='eliminarRuta' ),
    path('editarTramo/<int:cod_ruta>/<int:cod_tramo>', views.editarTramo, name ='editarTramo' ),
    path('eliminarTramo/<int:cod_ruta>/<int:cod_tramo>', views.eliminarTramo, name ='eliminarTramo' ),
    path('tramos/<int:cod_ruta>', views.tramos_by_ruta, name='tramo'),
]