# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# TODO Register your models here.

from .models import (Votos, Distrito, Candidato)

admin.site.register(Votos)
admin.site.register(Candidato)
admin.site.register(Distrito)