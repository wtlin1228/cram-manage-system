# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cram_api', '0009_auto_20170426_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='grade',
            field=models.CharField(choices=[('9', '國三'), ('8', '國二'), ('5', '小五'), ('12', '高三'), ('11', '高二'), ('7', '國一'), ('6', '小六'), ('10', '高一')], default='7', max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[('9', '國三'), ('8', '國二'), ('5', '小五'), ('12', '高三'), ('11', '高二'), ('7', '國一'), ('6', '小六'), ('10', '高一')], default='7', max_length=2),
        ),
        migrations.AlterField(
            model_name='studentcoursesigning',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='studentsibling',
            name='grade',
            field=models.CharField(choices=[('9', '國三'), ('8', '國二'), ('5', '小五'), ('12', '高三'), ('11', '高二'), ('7', '國一'), ('6', '小六'), ('10', '高一')], default='7', max_length=2),
        ),
    ]
