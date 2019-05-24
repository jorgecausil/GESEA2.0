#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Estudiantes, Programa, Inscripcion, AsistenciaEstudiante, Instructor, Ciclo
from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export import fields
from import_export.admin import ImportExportModelAdmin
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ('user',)
# Register your models here.


class EstudianteResource(resources.ModelResource):

	Programa_Academico = fields.Field(attribute='Programa_Academico',
								   widget=ForeignKeyWidget(Programa, 'nombre'))

	Ciclo_Lectivo = fields.Field(attribute='Ciclo_Lectivo',
								   widget=ForeignKeyWidget(Ciclo, 'ciclol'))

	class Meta:
		import_id_fields = ('ID_Estudiante','foto_url','Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido','Nro_Documento','Tipo_Documento','genero','Programa_Academico','Correo_Institucional','Nro_Telefonico','Ciclo_Lectivo','Descripcion')
		model = Estudiantes
		export_order = ('ID_Estudiante','foto_url','Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido','Nro_Documento','Tipo_Documento','genero','Programa_Academico','Correo_Institucional','Nro_Telefonico','Ciclo_Lectivo','Descripcion')
		fields = ('ID_Estudiante','foto_url','Primer_Nombre','Segundo_Nombre','Primer_Apellido','Segundo_Apellido','Nro_Documento','Tipo_Documento','genero','Programa_Academico','Correo_Institucional','Nro_Telefonico','Ciclo_Lectivo','Descripcion')


class EstudianteAdmin(ImportExportModelAdmin):

    # Opciones de visualización
    def reporte_asistencia(self, instance):
        return "<a href='/admin/reporte/%s'> <i style='font-size:17px' class='fa fa-file-pdf-o' aria-hidden='true'></i>  </a>" % instance.ID_Estudiante

    reporte_asistencia.short_description = "Reporte"
    reporte_asistencia.allow_tags = True
    reporte_asistencia.is_column = True

    search_fields = ('Primer_Apellido', 'Segundo_Apellido','Nro_Documento','Primer_Nombre', 'Segundo_Nombre', 'ID_Estudiante')
    list_filter = ('Ciclo_Lectivo','Programa_Academico')
    list_display = ['ID_Estudiante', 'Programa_Academico','Nro_Documento', 'Primer_Apellido', 'Segundo_Apellido', 'Primer_Nombre', 'Segundo_Nombre', 'Nro_Telefonico', 'reporte_asistencia']
    resource_class = EstudianteResource




class Inscripciones (admin.ModelAdmin):
    search_fields = ('estudiante__Primer_Nombre',)
    list_filter = ('programacion', 'fecha_inscripcion' )
    list_display = ['fecha_inscripcion','programacion', 'nombre_completo', 'id_ucc']
    raw_id_fields = ('estudiante', 'programacion' )

    def nombre_completo(self, obj):
     return obj.estudiante.Primer_Nombre + " " + obj.estudiante.Segundo_Nombre + " " + obj.estudiante.Primer_Apellido + " " + obj.estudiante.Segundo_Apellido

    def id_ucc(self, obj):
     return obj.estudiante.ID_Estudiante


class AsistenciaEstudianteAdmin (admin.ModelAdmin):
    search_fields = ('estudiante__Primer_Nombre',)
    list_filter = ('programacion', 'fecha_asistencia' )
    list_display = ['fecha_asistencia','programacion', 'nombre_completo', 'id_ucc']
    #readonly_fields = ('fecha_asistencia', 'asistio' )
    raw_id_fields = ('estudiante', 'programacion')

    def nombre_completo(self, obj):
     return obj.estudiante.Primer_Nombre + " " + obj.estudiante.Segundo_Nombre + " " + obj.estudiante.Primer_Apellido + " " + obj.estudiante.Segundo_Apellido

    def id_ucc(self, obj):
     return obj.estudiante.ID_Estudiante

class Instructores (admin.ModelAdmin):
	list_display = ['id_ucc','user','Identificacion','Nombre','Primer_Apellido','Segundo_Apellido','estado']
	class Meta:
		model = Instructor

admin.site.register(Instructor,Instructores)
admin.site.register(Inscripcion, Inscripciones)
admin.site.register(Estudiantes, EstudianteAdmin)
admin.site.register(Programa)
admin.site.register(Ciclo)
admin.site.register(AsistenciaEstudiante, AsistenciaEstudianteAdmin)
