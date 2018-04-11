# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-08 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0014_auto_20180408_0453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pipelineinstruction',
            old_name='immediate',
            new_name='firstparameter',
        ),
        migrations.RenameField(
            model_name='pipelineinstruction',
            old_name='offset',
            new_name='secondparameter',
        ),
        migrations.RemoveField(
            model_name='pipelineinstruction',
            name='rd',
        ),
        migrations.RemoveField(
            model_name='pipelineinstruction',
            name='rs',
        ),
        migrations.RemoveField(
            model_name='pipelineinstruction',
            name='rt',
        ),
        migrations.AddField(
            model_name='pipelineinstruction',
            name='thirdparameter',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
