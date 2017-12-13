# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Distrito(models.Model):
    """
    Se decide utilizar este modelo para la clase distrito porque es
    necesario el nombre y la cantidad de votantes,
    y en un futuro se mostrara un mapa con un marker por cada distrito
    que contenga los resultados del mismo.
    """
    nombre = models.CharField('Nombre del distrito', max_length=128)
    cantidad_votantes = models.IntegerField('Cantidad de votantes', default=0)
    latitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)
    longitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)


    def __str__(self):
        return '{}'.format(self.nombre)

class Candidato(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase
    """
    nombre = models.CharField('Nombre del candidato', max_length = 50)
    distrito = models.ForeignKey(Distrito, default = 0)
    votos_totales = models.IntegerField('Cantidad de votos', default = 0)
    votos_nulos = models.IntegerField('Cantidad de nulos', default = 0)
    porcentaje_votos = models.IntegerField('Porcentaje votos', default = 0)
    porcentaje_nulos = models.IntegerField('Porcentaje nulos', default = 0)
    def __str__(self):
        return '{} del distrito {}'.format(self.nombre, self.distrito)

class Voto(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase
    """
    candidato = models.ForeignKey(Candidato, default = 0)
    valido = models.BooleanField(null = False, default = 0)
