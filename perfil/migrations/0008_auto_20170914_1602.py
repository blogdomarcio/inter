# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0007_auto_20170914_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banheiro',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cozinha',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quarto',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sala',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
