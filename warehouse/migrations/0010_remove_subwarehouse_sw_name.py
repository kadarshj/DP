# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-31 08:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0009_auto_20180731_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subwarehouse',
            name='sw_name',
        ),
    ]
