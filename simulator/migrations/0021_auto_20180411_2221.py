# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-11 14:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0020_auto_20180411_2148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='CYCLE',
            new_name='ROW',
        ),
    ]