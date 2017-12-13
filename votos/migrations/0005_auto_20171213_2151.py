# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-13 21:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votos', '0004_auto_20171124_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valido', models.BooleanField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='votos',
            name='candidato',
        ),
        migrations.RemoveField(
            model_name='votos',
            name='distrito',
        ),
        migrations.RemoveField(
            model_name='votos',
            name='user',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='distrito_del_cadidato',
        ),
        migrations.AddField(
            model_name='candidato',
            name='distrito',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='votos.Distrito'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='porcentaje_nulos',
            field=models.IntegerField(default=0, verbose_name='Porcentaje nulos'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='porcentaje_votos',
            field=models.IntegerField(default=0, verbose_name='Porcentaje votos'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='votos_nulos',
            field=models.IntegerField(default=0, verbose_name='Cantidad de nulos'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='votos_totales',
            field=models.IntegerField(default=0, verbose_name='Cantidad de votos'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre del candidato'),
        ),
        migrations.AlterField(
            model_name='distrito',
            name='longitude',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=14, verbose_name='Latitud'),
        ),
        migrations.DeleteModel(
            name='Votos',
        ),
        migrations.AddField(
            model_name='voto',
            name='candidato',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='votos.Candidato'),
        ),
    ]
