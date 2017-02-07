# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

# Register your models here.
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad','sexo')
    search_fields = ['nombre',]
    list_filter = ['sexo',]

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente','fecha','programacion_cita')
    search_fields = ['paciente',]

class ResumenClinicoAdmin(admin.ModelAdmin):
    list_display = ('paciente',)
    search_fields = ['paciente',]

admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Consulta,ConsultaAdmin)
admin.site.register(ResumenClinico,ResumenClinicoAdmin)
