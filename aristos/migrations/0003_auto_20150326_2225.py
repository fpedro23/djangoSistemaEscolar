# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('aristos', '0002_auto_20150326_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='circular',
            options={'verbose_name_plural': 'Circulares'},
        ),
        migrations.RemoveField(
            model_name='evento',
            name='fechaPublicacion',
        ),
        migrations.AddField(
            model_name='evento',
            name='fechaFin',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 26, 22, 25, 20, 93348, tzinfo=utc), help_text=b'Fecha de Fin del Evento', verbose_name=b'Fecha de Fin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='fechaInicio',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 26, 22, 25, 35, 339259, tzinfo=utc), help_text=b'Fecha de Inicio del Evento', verbose_name=b'Fecha de Inicio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aviso',
            name='fechaPublicacion',
            field=models.DateField(verbose_name=b'Fecha de Publicaci\xc3\xb3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aviso',
            name='titulo',
            field=models.CharField(help_text=b'Titulo de el aviso', max_length=200, verbose_name=b'T\xc3\xadtulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='circular',
            name='fechaPublicacion',
            field=models.DateField(verbose_name=b'Fecha de Publicaci\xc3\xb3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='circular',
            name='titulo',
            field=models.CharField(help_text=b'T\xc3\xadtulo de la circular', max_length=200, verbose_name=b'T\xc3\xadtulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='titulo',
            field=models.CharField(help_text=b'Titulo de el evento', max_length=200, verbose_name=b'T\xc3\xadtulo'),
            preserve_default=True,
        ),
    ]
