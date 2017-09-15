# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 02:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0008_auto_20170914_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Externa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagens/externa')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('estilo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.Estilo')),
            ],
        ),
        migrations.CreateModel(
            name='Lavabo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagens/lavabo')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('estilo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.Estilo')),
            ],
        ),
        migrations.CreateModel(
            name='Lavanderia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagens/lavanderia')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('estilo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.Estilo')),
            ],
        ),
        migrations.CreateModel(
            name='Outros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagens/outros')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('estilo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.Estilo')),
            ],
        ),
        migrations.CreateModel(
            name='Varanda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagens/varanda')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('estilo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.Estilo')),
            ],
        ),
        migrations.RemoveField(
            model_name='banheiro',
            name='estilo',
        ),
        migrations.DeleteModel(
            name='Banheiro',
        ),
    ]
