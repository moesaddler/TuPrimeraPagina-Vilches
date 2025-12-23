from django.db import models

class DepartamentoMedico(models.Model):
    nombre = models.CharField(max_length=50)
    nro_dpto = models.IntegerField(unique=True)
    nro_empleados = models.IntegerField(null=True)
    fecha_de_creacion = models.DateField(auto_now_add=True)
    email_dpto = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} / Nro_dpto: {self.nro_dpto}"


"""
from ambulance.models import DepartamentoMedico
departamento = DepartamentoMedico.objects.create(nombre ="Traumatologia", nro_dpto=2, nro_empleados=12, email_dpto="
trauma@gmail.com")
departamento
<DepartamentoMedico: Nombre: Traumatologia / Nro_dpto: 2>
departamento.fecha_de_creacion
datetime.date(2025, 12, 23)
departamento2 = DepartamentoMedico.objects.create(nombre ="Radiologia", nro_dpto=3, nro_empleados=5, email_dpto="radio@gmail.com")              
departamento2
<DepartamentoMedico: Nombre: Radiologia / Nro_dpto: 3>
departamento2.save()
 exit()"""