# -*- coding: UTF-8 -*-
from django.db import models
from models import *
from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets

class EmailForm(forms.Form):
      name = forms.CharField(max_length=255)
      email = forms.EmailField()
      phone = forms.IntegerField()
      message = forms.CharField(widget=forms.Textarea)

class ConsultaForm(forms.Form):
    paciente = forms.IntegerField()
    fecha = forms.DateTimeField(widget = widgets.AdminSplitDateTime())
    motivo = forms.CharField(widget=forms.Textarea)
    examen_fisico = forms.CharField(widget=forms.Textarea)
    examen = forms.CharField(widget=forms.Textarea,required=False)
    tratamiento = forms.CharField(widget=forms.Textarea,required=False)
    programacion_cita = forms.DateTimeField(required=False)
    costo = forms.FloatField()
