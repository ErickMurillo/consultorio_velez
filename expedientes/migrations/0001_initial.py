# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('motivo', ckeditor.fields.RichTextField()),
                ('examen_fisico', ckeditor.fields.RichTextField()),
                ('examen', ckeditor.fields.RichTextField(null=True, blank=True)),
                ('tratamiento', ckeditor.fields.RichTextField(null=True, blank=True)),
                ('programacion_cita', models.DateTimeField(null=True, blank=True)),
                ('costo', models.FloatField(verbose_name=b'Costo (C$)')),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
                ('edad', models.IntegerField(verbose_name=b'Edad (A\xc3\xb1os)')),
                ('sexo', models.IntegerField(choices=[(1, b'Femenino'), (2, b'Masculino')])),
                ('nacionalidad', models.CharField(max_length=100, null=True, blank=True)),
                ('telefono', models.CharField(max_length=100, null=True, blank=True)),
                ('antecedentes', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(to='expedientes.Paciente'),
        ),
    ]
