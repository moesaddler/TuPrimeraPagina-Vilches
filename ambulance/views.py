from django.shortcuts import render
from ambulance.models import DepartamentoMedico

def home(request):
    return render(request, "ambulance/index.html")

def listar_dptos(request):
    departamentos_query = DepartamentoMedico.objects.all() # list(QuerySet[dpto, ..., dpto, ...])
    contexto = {
        "departamentos": departamentos_query
    }
    return render(request, "ambulance/departamentos_medicos.html", contexto)