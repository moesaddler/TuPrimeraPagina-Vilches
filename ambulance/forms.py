# ambulance/forms.py
from django import forms
from .models import Clase, Profesor, Alumno

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = '__all__'

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'especialidad']

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'edad', 'email']




