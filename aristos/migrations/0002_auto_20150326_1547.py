# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aristos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aviso',
            name='remitente',
            field=models.ForeignKey(default=1, to='aristos.Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='circular',
            name='remitente',
            field=models.ForeignKey(default=1, to='aristos.Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='remitente',
            field=models.ForeignKey(default=1, to='aristos.Usuario'),
            preserve_default=False,
        ),
    ]
