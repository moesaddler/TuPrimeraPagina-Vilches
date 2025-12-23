# ambulance/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('clases/', views.listar_clases, name='listar_clases'),
    path('profesores/', views.listar_profesores, name='listar_profesores'),
    path('alumnos/', views.listar_alumnos, name='listar_alumnos'),

    path('profesores/crear/', views.crear_profesor, name='crear_profesor'),
    path('clases/crear/', views.crear_clase, name='crear_clase'),
    path('alumnos/crear/', views.crear_alumno, name='crear_alumno'),
]
