# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postagens', '0002_postagem_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='postagem',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='postagem',
            name='descricao',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
