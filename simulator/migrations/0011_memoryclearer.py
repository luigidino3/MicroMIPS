# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-28 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0010_auto_20180327_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemoryClearer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(default=0)),
            ],
        ),
    ]