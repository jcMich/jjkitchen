# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usedingredient',
            name='unit',
            field=models.CharField(choices=[('KG', 'Kilo'), ('GR', 'Gramo'), ('LT', 'Litro'), ('PZ', 'Pizca'), ('TR', 'Trozo'), ('HJ', 'Hoja'), ('RM', 'Rama'), ('CD', 'Cuadro'), ('PZ', 'Pieza'), ('UN', 'Unidad')], max_length=1),
        ),
    ]
