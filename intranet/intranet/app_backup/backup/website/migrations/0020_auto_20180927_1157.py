# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-27 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_auto_20180926_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_end_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
