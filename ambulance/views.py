# ambulance/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Clase, Profesor, Alumno
from .forms import ClaseForm, ProfesorForm, AlumnoForm


def inicio(request):
    return render(request, 'ambulance/inicio.html')

# Listados
def listar_clases(request):
    clases = Clase.objects.all()
    return render(request, 'ambulance/listar_clases.html', {'clases': clases})

def listar_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'ambulance/listar_profesores.html', {'profesores': profesores})

def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'ambulance/listar_alumnos.html', {'alumnos': alumnos})

# Crear registros
def crear_clase(request):
    form = ClaseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_clases')
    return render(request, 'ambulance/form_clase.html', {'form': form})

def crear_profesor(request):
    form = ProfesorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_profesores')
    return render(request, 'ambulance/form_profesor.html', {'form': form})

def crear_alumno(request):
    form = AlumnoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_alumnos')
    return render(request, 'ambulance/form_alumno.html', {'form': form})



