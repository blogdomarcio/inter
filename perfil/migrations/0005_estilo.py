# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_auto_20170914_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estilo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagens/estilo')),
            ],
        ),
    ]
