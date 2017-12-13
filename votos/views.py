# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from votos.models import *


def resultado_global(request):
    """
    Generar la vista para devolver el resultado global de la elección.
    Tener en cuenta que tiene que tener:
    Cantidad total de votos por candidato
    Cantidad total de votos nulos
    Porcentaje de cada candidato
    Porcentaje de votos nulos
    Total de votos de la elección
    """
    
    #TODO TU CODIGO AQUI

    votos_candidatos = Candidato.objects.all().order_by('-votos_totales')
    candidato = Candidato.objects.all()
    voto = Voto.objects.all()
    distrito = Distrito.objects.all()
    porcentaje_nulos = Voto.objects.filter(candidato = candidato, valido = False).count() * 100 / Voto.objects.count()
    votos_nulos = Voto.objects.filter(candidato = candidato, valido = False).count()
    total = Voto.objects.count()

    for candidato in votos_candidatos:
        candidato.votos_totales = Voto.objects.filter(candidato = candidato, valido = True).count()
        candidato.porcentaje_votos = Voto.objects.filter(candidato = candidato, valido = True).count() * 100 / Voto.objects.count()
        candidato.save()
    return render(request,'global.html', {'candidato':candidato, 'votos_candidatos':votos_candidatos, 'voto':voto, 'distritos':distrito, 'porcentaje_nulos':porcentaje_nulos, 'votos_nulos':votos_nulos, 'total':total})


def distrital(request, id_distrito):
    """
    Generar la vista para devolver el resultado distrital de la elección
    Tener en cuenta que tiene que tener:
    Tamaño del padrón
    Porcentaje de votos del distrito (respecto al padron. Ejemplo: Si el distrito tiene 1000 votantes y hay 750 votos, el porcentaje es 75%)
    Total de votos del distrito
    Candidato ganador
    """

    #TODO TU CODIGO AQUI

    distrito = Distrito.objects.get(id=id_distrito)
    total_votantes = Voto.objects.filter(candidato__distrito = distrito).count()
    padron = distrito.cantidad_votantes
    porcentaje_votantes = Voto.objects.filter(candidato__distrito = distrito).count()*100/padron
    candidato = Candidato.objects.filter(distrito=distrito, votos_totales__gt=0)
    for c in candidato[:1]:
        ganador = c.nombre
    return render(request,'distrital.html', {'distrito':distrito, 'padron':padron, 'porcentaje_votantes':porcentaje_votantes, 'total_votantes':total_votantes, 'ganador':ganador})
