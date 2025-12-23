from django.urls import path
from ambulance.views import *


urlpatterns = [
    path("", home, name="home"),
    path("lista_departamentos", listar_dptos, name="departament_list"),
]