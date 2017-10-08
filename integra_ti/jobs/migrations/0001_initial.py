# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('company_adress', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('earnings', models.DecimalField(decimal_places=2, max_digits=6)),
                ('link', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
    ]
