# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
SEXO_CHOICES = ((1,'Femenino'),(2,'Masculino'))

class Paciente(models.Model):
    nombre = models.CharField(max_length=250)
    edad = models.IntegerField(verbose_name='Edad (Años)')
    sexo = models.IntegerField(choices=SEXO_CHOICES)
    nacionalidad = models.CharField(max_length=100,null=True,blank=True)
    telefono = models.CharField(max_length=100,null=True,blank=True)
    antecedentes = RichTextUploadingField()
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.nombre))
        super(Paciente, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
		return self.nombre

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente)
    fecha = models.DateTimeField()
    motivo = RichTextField()
    examen_fisico = RichTextField()
    examen = RichTextField(null=True,blank=True)
    tratamiento = RichTextField(null=True,blank=True)
    programacion_cita = models.DateTimeField(null=True,blank=True)
    costo = models.FloatField(verbose_name='Costo (C$)')

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

    def __str__(self):
		return self.paciente.nombre

class ResumenClinico(models.Model):
    paciente = models.ForeignKey(Paciente)
    fecha = models.DateField()
    resumen = RichTextField()

    class Meta:
        verbose_name = 'Resumen clínico'
        verbose_name_plural = 'Resúmenes clínicos'

    def __str__(self):
		return self.paciente.nombre
