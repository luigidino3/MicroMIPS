# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-11 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0023_memorycomparer'),
    ]

    operations = [
        migrations.AddField(
            model_name='memorycomparer',
            name='memoryType',
            field=models.IntegerField(default=0),
        ),
    ]
