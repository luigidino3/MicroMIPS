# Generated by Django 2.0.2 on 2018-04-11 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0018_auto_20180411_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CIF', models.IntegerField(default=0)),
                ('CID', models.IntegerField(default=0)),
                ('CEX', models.IntegerField(default=0)),
                ('CMEM', models.IntegerField(default=0)),
                ('CWB', models.IntegerField(default=0)),
                ('CYCLE', models.IntegerField(default=0)),
                ('CSTALL', models.IntegerField(default=0)),
                ('POSITION', models.IntegerField(default=0)),
                ('SPACE', models.IntegerField(default=0)),
            ],
        ),
    ]
