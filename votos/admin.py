# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# TODO Register your models here.

admin.site.register(Distrito)
admin.site.register(Candidato)
admin.site.register(Voto)