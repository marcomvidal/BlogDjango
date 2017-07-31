# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postagens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postagem',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
