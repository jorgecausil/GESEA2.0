# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-05-12 01:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actividades', '0001_initial'),
        ('inscripcion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaActividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dia_Actividad', models.CharField(choices=[('LUNES', 'Lunes'), ('MARTES', 'Martes'), ('MIERCOLES', 'Miercoles'), ('JUEVES', 'Jueves'), ('VIERNES', 'Viernes'), ('SABADO', 'Sabado'), ('DOMINGO', 'Domingo')], max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Dias Actividades',
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hora_Inicio', models.TimeField(null=True)),
                ('Hora_Final', models.TimeField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Horas',
            },
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreLugar', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Lugares',
            },
        ),
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipodeParticipacion', models.CharField(choices=[('CURSO', 'Curso'), ('GRUPO DE REPRESENTACION', 'Grupo de representacion'), ('EQUIPOS DE REPRESENTACION', 'Equipos de representacion'), ('BRIGADA', 'Brigada'), ('OTRO', 'Otro')], max_length=30)),
                ('Fecha_Inicio', models.DateTimeField(null=True)),
                ('Fecha_Final', models.DateTimeField(null=True)),
                ('Dia_semana', models.ManyToManyField(to='programacion.DiaActividad')),
                ('Instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inscripcion.Instructor')),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividades.Actividad')),
                ('lugarActividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programacion.Lugar')),
            ],
            options={
                'verbose_name': 'Actividad Creada',
                'verbose_name_plural': 'Actividades Creadas',
            },
        ),
        migrations.AddField(
            model_name='diaactividad',
            name='Horario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programacion.Horario'),
        ),
    ]
