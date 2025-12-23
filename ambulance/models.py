# ambulance/models.py
from django.db import models

class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()
    matricula = models.CharField(max_length=20)
    clase = models.ForeignKey('Clase', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"



