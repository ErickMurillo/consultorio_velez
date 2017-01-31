# -*- coding: UTF-8 -*-
from django.db import models
from models import *
from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets
from expedientes.models import *

class EmailForm(forms.Form):
      name = forms.CharField(max_length=255)
      email = forms.EmailField()
      phone = forms.IntegerField()
      message = forms.CharField(widget=forms.Textarea)

class ConsultaForm(forms.ModelForm):
    fecha = forms.DateTimeField(widget = widgets.AdminSplitDateTime())
    programacion_cita = forms.DateTimeField(widget = widgets.AdminSplitDateTime())
    class Meta:
        model = Consulta
        fields = '__all__'
