# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-19 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0005_datasegment'),
    ]

    operations = [
        migrations.CreateModel(
            name='MipsProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4)),
                ('value', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
    ]