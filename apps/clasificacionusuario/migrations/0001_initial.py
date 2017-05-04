# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 23:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persona', '0001_initial'),
        ('tipo_usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacionusuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='persona.Persona')),
                ('tipouser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tipo_usuario.Tipo_usuario')),
            ],
        ),
    ]