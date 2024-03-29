# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-31 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0011_auto_20180731_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assemblywarehouse',
            name='end_transport',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='assemblywarehouse',
            name='return_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='assemblywarehouse',
            name='start_transport',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='citywarehouse',
            name='end_transport',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='citywarehouse',
            name='return_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='citywarehouse',
            name='start_transport',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='subwarehouse',
            name='end_transport',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='subwarehouse',
            name='return_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='subwarehouse',
            name='start_transport',
            field=models.DateTimeField(blank=True),
        ),
    ]
