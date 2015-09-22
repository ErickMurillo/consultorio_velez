# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
from especialidades.utils import get_file_path

# Create your models here.
CATEGORIA_CHOICES = (
	(1,'Ortopedia'),
	(2,'Trauma'),
	(3,'Artroscopia'),
	(4,'Cirugía Biológica'),
	)

class Casos(models.Model):
	titulo =  models.CharField(max_length=200)
	categoria = models.IntegerField(choices=CATEGORIA_CHOICES)
	descripcion = RichTextField()
	video = models.URLField(blank=True,null=True,verbose_name='Url del video (opcional)')

	class Meta:
        verbose_name = 'Caso médico'
        verbose_name_plural = 'Casos médicos'

class SubirFotos(models.Model):
	imagen = models.ImageField()
	casos = models.ForeignKey(Casos)

	fileDir = 'media/'