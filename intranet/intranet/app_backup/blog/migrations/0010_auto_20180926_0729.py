# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-26 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='department',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
