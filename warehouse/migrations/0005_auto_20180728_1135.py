# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-28 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0004_citywarehouse_subwarehouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='subwarehouse',
            name='cust_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='subwarehouse',
            name='cust_phoneno',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]