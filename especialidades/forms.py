# -*- coding: UTF-8 -*-
from django.db import models
from models import *
from django import forms
from django.forms import ModelForm

class EmailForm(forms.Form):
      name = forms.CharField(max_length=255)
      email = forms.EmailField()
      phone = forms.IntegerField()
      message = forms.CharField(widget=forms.Textarea)