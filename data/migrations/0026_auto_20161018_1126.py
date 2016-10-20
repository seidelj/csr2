# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-18 16:26
from __future__ import unicode_literals

import data.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0025_auto_20161018_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatmentcell',
            name='msg',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='timestarted',
            field=models.DateTimeField(default=data.models.get_now),
        ),
    ]