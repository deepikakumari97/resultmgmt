# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-01 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rollNo',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
