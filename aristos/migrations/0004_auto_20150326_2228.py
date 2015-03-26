# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aristos', '0003_auto_20150326_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fechaFin',
            field=models.DateTimeField(help_text=b'Fecha de Fin del Evento', null=True, verbose_name=b'Fecha de Fin (HH:MM)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fechaInicio',
            field=models.DateTimeField(help_text=b'Fecha de Inicio del Evento', null=True, verbose_name=b'Fecha de Inicio (HH:MM)', blank=True),
            preserve_default=True,
        ),
    ]
