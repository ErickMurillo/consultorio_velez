# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('expedientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumenClinico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('resumen', ckeditor.fields.RichTextField()),
                ('paciente', models.ForeignKey(to='expedientes.Paciente')),
            ],
            options={
                'verbose_name': 'Resumen cl\xednico',
                'verbose_name_plural': 'Res\xfamenes cl\xednicos',
            },
        ),
    ]
