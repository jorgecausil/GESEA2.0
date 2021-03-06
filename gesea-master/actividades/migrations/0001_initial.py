# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-05-12 01:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo_actividad', models.CharField(max_length=10, unique=True)),
                ('tipo_actividad', models.CharField(max_length=80, null=True)),
                ('Estado_actividad', models.CharField(choices=[('ABIERTA', 'Abierta'), ('CERRADA', 'Cerrada')], default='ABIERTA', max_length=30)),
                ('Cupo_Actividad', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Actividades',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo_area', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='actividad',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividades.Area'),
        ),
    ]
