from django.db import models
#Modelo de la clase servicio
class Area(models.Model):
    Codigo_area = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return str(self.nombre)

#Modelo de la clase actividad
class Actividad(models.Model):

    ESTADOS_ACTIVIDAD = (
        ('ABIERTA', 'Abierta'),
        ('CERRADA', 'Cerrada'),
    )
    area =  models.ForeignKey(Area)
    Codigo_actividad = models.CharField(max_length=10, unique=True)
    tipo_actividad = models.CharField(max_length=80, null=True)
    Estado_actividad =  models.CharField(max_length=30, choices=ESTADOS_ACTIVIDAD, default='ABIERTA')
    Cupo_Actividad = models.IntegerField()
    class Meta:
        verbose_name_plural = "Actividades"
    def __str__(self):
        return str(self.tipo_actividad)

#Modelo de la clase registro de actividad
# class RegistroActividad(models.Model):
#     area =  models.ForeignKey(Area)
#     actividad =  models.ForeignKey(Actividad)
#     class Meta:
#         verbose_name_plural = "Registro Actividad"
#
#     def __str__(self):
#         return str(self.actividad)
