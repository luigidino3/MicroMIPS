# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-11 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0016_auto_20180411_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ex',
            old_name='name',
            new_name='cycle',
        ),
        migrations.RenameField(
            model_name='id',
            old_name='name',
            new_name='cycle',
        ),
        migrations.RenameField(
            model_name='if',
            old_name='name',
            new_name='cycle',
        ),
        migrations.RenameField(
            model_name='mem',
            old_name='name',
            new_name='cycle',
        ),
        migrations.RenameField(
            model_name='stall',
            old_name='name',
            new_name='cycle',
        ),
        migrations.RenameField(
            model_name='wb',
            old_name='name',
            new_name='cycle',
        ),
        migrations.RemoveField(
            model_name='ex',
            name='opcode',
        ),
        migrations.RemoveField(
            model_name='id',
            name='opcode',
        ),
        migrations.RemoveField(
            model_name='if',
            name='opcode',
        ),
        migrations.RemoveField(
            model_name='mem',
            name='opcode',
        ),
        migrations.RemoveField(
            model_name='wb',
            name='opcode',
        ),
        migrations.AddField(
            model_name='ex',
            name='row',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='id',
            name='row',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='if',
            name='row',
            field=models.IntegerField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='mem',
            name='row',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mipsprogram',
            name='opcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='stall',
            name='row',
            field=models.IntegerField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='wb',
            name='row',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ex',
            name='aluoutput',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='ex',
            name='b',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='ex',
            name='cond',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='id',
            name='a',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='id',
            name='b',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='id',
            name='imm',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='id',
            name='npc',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='if',
            name='npc',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='if',
            name='pc',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='mem',
            name='aluoutput',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='mem',
            name='lmd',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='mem',
            name='memoryrange',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='wb',
            name='result',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
