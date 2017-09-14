# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banheiro',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/modelos/banheiros'),
        ),
        migrations.AlterField(
            model_name='cozinha',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/modelos/cozinha'),
        ),
        migrations.AlterField(
            model_name='quarto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/modelos/quarto'),
        ),
        migrations.AlterField(
            model_name='sala',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/modelos/sala'),
        ),
    ]