# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-02 20:34
from __future__ import unicode_literals

import data.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20160202_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='address',
            field=models.CharField(max_length=768, null=True, verbose_name=b'Street Address'),
        ),
        migrations.AlterField(
            model_name='task',
            name='broken_signs',
            field=models.IntegerField(choices=[(0, b'No'), (1, b'Yes'), (2, b'N/A')], null=True, verbose_name=b'Broken Street Signs'),
        ),
        migrations.AlterField(
            model_name='task',
            name='bui_quality',
            field=models.IntegerField(choices=[(1, b'Strongly Disagree'), (2, b'Disagree'), (3, b'Neither Agree or Disagree'), (4, b'Agree'), (5, b'Stronly Agree'), (6, b'N/A')], null=True, verbose_name=b'Building Quality'),
        ),
        migrations.AlterField(
            model_name='task',
            name='car_quality',
            field=models.IntegerField(choices=[(1, b'Strongly Disagree'), (2, b'Disagree'), (3, b'Neither Agree or Disagree'), (4, b'Agree'), (5, b'Stronly Agree'), (6, b'N/A')], null=True, verbose_name=b'Car Quality'),
        ),
        migrations.AlterField(
            model_name='task',
            name='for_sale',
            field=models.IntegerField(choices=[(0, b'No'), (1, b'Yes'), (2, b'N/A')], null=True, verbose_name=b'Houses for sale signs'),
        ),
        migrations.AlterField(
            model_name='task',
            name='litter',
            field=models.IntegerField(choices=[(1, b'Strongly Disagree'), (2, b'Disagree'), (3, b'Neither Agree or Disagree'), (4, b'Agree'), (5, b'Stronly Agree'), (6, b'N/A')], null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='month',
            field=models.IntegerField(choices=[(1, b'Jan'), (2, b'Feb'), (3, b'Mar'), (4, b'Apr'), (5, b'May'), (6, b'Jun'), (7, b'Jul'), (8, b'Aug'), (9, b'Sep'), (10, b'Oct'), (11, b'Nov'), (12, b'Dec')], null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='people',
            field=models.IntegerField(choices=[(0, b'No'), (1, b'Yes'), (2, b'N/A')], null=True, verbose_name=b'People actively covering faces'),
        ),
        migrations.AlterField(
            model_name='task',
            name='pic_quality',
            field=models.IntegerField(choices=[(1, b'Strongly Disagree'), (2, b'Disagree'), (3, b'Neither Agree or Disagree'), (4, b'Agree'), (5, b'Stronly Agree'), (6, b'N/A')], null=True, verbose_name=b'Picture Quality'),
        ),
        migrations.AlterField(
            model_name='task',
            name='pot_holes',
            field=models.IntegerField(choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'5+'), (7, b'N/A')], null=True, verbose_name=b'Pot Holes'),
        ),
        migrations.AlterField(
            model_name='task',
            name='road_work',
            field=models.IntegerField(choices=[(0, b'No'), (1, b'Yes'), (2, b'N/A')], null=True, verbose_name=b'Road Work'),
        ),
        migrations.AlterField(
            model_name='task',
            name='shoes',
            field=models.IntegerField(choices=[(0, b'No'), (1, b'Yes'), (2, b'N/A')], null=True, verbose_name=b'Shoes on wire'),
        ),
        migrations.AlterField(
            model_name='task',
            name='str_quality',
            field=models.IntegerField(choices=[(1, b'Strongly Disagree'), (2, b'Disagree'), (3, b'Neither Agree or Disagree'), (4, b'Agree'), (5, b'Stronly Agree'), (6, b'N/A')], null=True, verbose_name=b'Street Quality'),
        ),
        migrations.AlterField(
            model_name='task',
            name='timestarted',
            field=models.DateTimeField(default=data.models.get_now),
        ),
        migrations.AlterField(
            model_name='task',
            name='trees',
            field=models.IntegerField(choices=[(0, b'No'), (1, b'Yes'), (2, b'N/A')], null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='year',
            field=models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)], null=True),
        ),
    ]
