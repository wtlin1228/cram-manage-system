# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cram_api', '0014_auto_20170503_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentstudysigning',
            name='seat',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='grade',
            field=models.CharField(choices=[('7', '國一'), ('12', '高三'), ('11', '高二'), ('5', '小五'), ('10', '高一'), ('9', '國三'), ('6', '小六'), ('8', '國二')], default='7', max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[('7', '國一'), ('12', '高三'), ('11', '高二'), ('5', '小五'), ('10', '高一'), ('9', '國三'), ('6', '小六'), ('8', '國二')], default='7', max_length=2),
        ),
        migrations.AlterField(
            model_name='studentsibling',
            name='grade',
            field=models.CharField(choices=[('7', '國一'), ('12', '高三'), ('11', '高二'), ('5', '小五'), ('10', '高一'), ('9', '國三'), ('6', '小六'), ('8', '國二')], default='7', max_length=2),
        ),
    ]
