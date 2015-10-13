# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from sorl.thumbnail.admin import AdminImageMixin

# Register your models here.

class Fotos_Inline(AdminImageMixin, admin.TabularInline):
	model = SubirFotos
	max_num = 16
	can_delete = True

class CasosAdmin(admin.ModelAdmin):
	inlines = [Fotos_Inline]


admin.site.register(Casos,CasosAdmin)
admin.site.register(Informacion)
admin.site.register(Experiencia)
