from django.contrib import admin
from ambulance.models import *

#admin.site.register(DepartamentoMedico)

@admin.register(DepartamentoMedico)
class DepartamentoMedicoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "nro_dpto", "email_dpto", "fecha_de_creacion")
    list_display_links = ("nombre",)
    search_fields = ("nro_dpto",)
    list_filter = ("fecha_de_creacion",)
    ordering = ("nro_dpto", "nombre")
    readonly_fields = ("fecha_de_creacion",)


# Register your models here.
