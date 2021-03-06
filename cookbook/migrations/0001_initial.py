# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-03 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('slug', models.SlugField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('note', models.CharField(blank=True, max_length=500, null=True)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='/')),
                ('cook_time', models.TimeField(blank=True, null=True)),
                ('dificult', models.CharField(choices=[('E', 'Easy'), ('M', 'Medium'), ('D', 'Difucult')], default='M', max_length=1)),
                ('directions', models.TextField()),
                ('cook_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UsedIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used', models.FloatField()),
                ('unit', models.CharField(choices=[('K', 'Kilo'), ('G', 'Gramo'), ('L', 'Litro'), ('P', 'Pizca'), ('T', 'Trozo'), ('H', 'Hoja'), ('R', 'Rama'), ('C', 'Cuadro')], max_length=1)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='cookbook.UsedIngredient'),
        ),
    ]
