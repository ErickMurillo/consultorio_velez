# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from especialidades.utils import get_file_path
from sorl.thumbnail import ImageField

# Create your models here.
CATEGORIA_CHOICES = (
	(1,'Ortopedia'),
	(2,'Trauma'),
	(3,'Artroscopia'),
	(4,'Cirugía Biológica'),
	)

class Casos(models.Model):
	titulo =  models.CharField(max_length=450)
	slug = models.SlugField(editable=False, max_length=450)
	categoria = models.IntegerField(choices=CATEGORIA_CHOICES)
	descripcion = RichTextField()
	video = models.URLField(blank=True,null=True,verbose_name='Url del video (opcional)')

	def __unicode__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		self.slug = (slugify(self.titulo))
		super(Casos, self).save(*args, **kwargs)
		
	class Meta:
		verbose_name = 'Caso médico'
		verbose_name_plural = 'Casos médicos'

class SubirFotos(models.Model):
	imagen = ImageField(upload_to=get_file_path)
	casos = models.ForeignKey(Casos)

	fileDir = 'fotos/'

	class Meta:
		verbose_name = 'Foto'
		verbose_name_plural = 'Fotos'

class Informacion(models.Model):
	descripcion = RichTextField()

	class Meta:
		verbose_name = 'Información'
		verbose_name_plural = 'Información'

class Experiencia(models.Model):
	descripcion = RichTextField()

	class Meta:
		verbose_name = 'Experiencia'
		verbose_name_plural = 'Experiencias'
