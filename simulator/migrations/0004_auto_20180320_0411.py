# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-19 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0003_register_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='value',
            field=models.CharField(max_length=16),
        ),
    ]
