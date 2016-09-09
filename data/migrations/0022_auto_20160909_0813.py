# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-09 13:13
from __future__ import unicode_literals

import data.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0021_auto_20160908_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='mturker',
            name='batchOrder',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='treatmentcell',
            name='imageLimit',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='mturker',
            name='start',
            field=models.DateTimeField(default=data.models.get_now),
        ),
        migrations.AlterField(
            model_name='task',
            name='timestarted',
            field=models.DateTimeField(default=data.models.get_now),
        ),
        migrations.AlterField(
            model_name='treatmentcell',
            name='batch',
            field=models.CharField(default=datetime.datetime(2016, 9, 9, 13, 13, 51, 203795, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
    ]
