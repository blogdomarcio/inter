# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banheiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='banheiros')),
                ('descricao', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cozinha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='cozinha')),
                ('descricao', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='quarto')),
                ('descricao', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='sala')),
                ('descricao', models.TextField(null=True)),
            ],
        ),
    ]
