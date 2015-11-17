# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('especialidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experiencia',
            options={'verbose_name': 'Experiencia', 'verbose_name_plural': 'Experiencias'},
        ),
        migrations.AddField(
            model_name='subirfotos',
            name='comentario',
            field=models.CharField(max_length=400, null=True, blank=True),
        ),
    ]
