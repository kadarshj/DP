# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-27 11:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssemblyWarehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purifierid', models.CharField(max_length=10, unique=True)),
                ('aw_manager', models.CharField(max_length=250)),
                ('aw_executive', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('is_in_transport', models.CharField(choices=[('Hold', 'Hold'), ('Transit', 'Transit'), ('Shifted', 'Shifted')], default='Hold', max_length=25)),
                ('is_in_citywarehouse', models.BooleanField(default=False)),
                ('transport_person_name', models.CharField(max_length=250)),
                ('is_returned', models.BooleanField(default=False)),
                ('returned_from', models.CharField(max_length=250)),
                ('is_device_ok', models.BooleanField(max_length=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]