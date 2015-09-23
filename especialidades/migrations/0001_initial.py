# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import especialidades.utils
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=450)),
                ('slug', models.SlugField(max_length=450, editable=False)),
                ('categoria', models.IntegerField(choices=[(1, b'Ortopedia'), (2, b'Trauma'), (3, b'Artroscopia'), (4, b'Cirug\xc3\xada Biol\xc3\xb3gica')])),
                ('descripcion', ckeditor.fields.RichTextField()),
                ('video', models.URLField(null=True, verbose_name=b'Url del video (opcional)', blank=True)),
            ],
            options={
                'verbose_name': 'Caso m\xe9dico',
                'verbose_name_plural': 'Casos m\xe9dicos',
            },
        ),
        migrations.CreateModel(
            name='SubirFotos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', sorl.thumbnail.fields.ImageField(upload_to=especialidades.utils.get_file_path)),
                ('casos', models.ForeignKey(to='especialidades.Casos')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
            },
        ),
    ]
