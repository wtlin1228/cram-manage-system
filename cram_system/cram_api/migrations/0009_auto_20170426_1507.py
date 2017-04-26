# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cram_api', '0008_auto_20170426_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='grade',
            field=models.CharField(choices=[('12', '高三'), ('8', '國二'), ('11', '高二'), ('5', '小五'), ('9', '國三'), ('10', '高一'), ('6', '小六'), ('7', '國一')], default='7', max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[('12', '高三'), ('8', '國二'), ('11', '高二'), ('5', '小五'), ('9', '國三'), ('10', '高一'), ('6', '小六'), ('7', '國一')], default='7', max_length=2),
        ),
        migrations.AlterField(
            model_name='studentsibling',
            name='grade',
            field=models.CharField(choices=[('12', '高三'), ('8', '國二'), ('11', '高二'), ('5', '小五'), ('9', '國三'), ('10', '高一'), ('6', '小六'), ('7', '國一')], default='7', max_length=2),
        ),
    ]
