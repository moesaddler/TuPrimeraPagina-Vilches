# ambulance/admin.py
from django.contrib import admin
from .models import Clase, Profesor, Alumno

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'fecha_creacion')
    ordering = ('nombre',)
    readonly_fields = ('fecha_creacion',)
    search_fields = ('nombre', 'codigo')

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')
    ordering = ('apellido',)
    search_fields = ('nombre', 'apellido', 'email')

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'matricula', 'clase')
    ordering = ('apellido',)
    search_fields = ('nombre', 'apellido', 'matricula')


