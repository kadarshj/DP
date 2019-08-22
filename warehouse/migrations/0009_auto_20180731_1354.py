# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-31 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0008_auto_20180730_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='assemblywarehouse',
            name='cw_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='citywarehouse',
            name='sw_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='subwarehouse',
            name='sw_name',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
