# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 22:13
from __future__ import unicode_literals

import data.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_auto_20160622_1712'),
    ]

    operations = [
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
    ]
