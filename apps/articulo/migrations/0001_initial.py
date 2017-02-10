# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-09 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='media/pictures')),
                ('fecha_publicacion', models.DateField(blank=True, null=True)),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('articulo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.Articulo')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='tag',
            field=models.ManyToManyField(to='articulo.Tag'),
        ),
    ]
