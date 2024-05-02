'''Modelos para las bases de datos'''
from datetime import datetime
from django.db import models

# Create your models here.

class Taxis(models.Model):
    '''Modelo para taxis, el campo id tiene relacion con el modelo trajectorias'''
    id = models.AutoField(primary_key=True)
    #unique = True especifica que los campos deben ser unicos y no repetirse
    plate = models.CharField(max_length=20)
    #max_length= ? revisar cuantos caracteres pueden aceptars
    class Meta:
        '''La clase metadata es cualquier cosa que no sea un campo como opciones de orten, 
        nombre de la BD o nombres singulares o plurales legibles por humanos (verbose_name),
          esto es completamente opcional '''
        verbose_name_plural = "taxis"
    def __str__(self) -> str:
        return self.plate

class Trajectories(models.Model):
    '''modelo y campos para trajectorias'''
    id = models.AutoField(primary_key=True)
    taxi_id = models.ForeignKey(Taxis, on_delete=models.CASCADE, db_column='taxi_id')
    #foreignkey requiere un argumento que seria la clase del modelo con el que está relacionado
    date = models.DateTimeField()#auto_now=True
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        '''las clases metas son opcionales'''
        verbose_name_plural="trajectories"
    
    def __str__(self):
        return datetime.strftime(self.date, '%Y-%m-%d %H:%M:%S')
    