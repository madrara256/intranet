# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-07 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0007_auto_20180907_0601'),
        ('website', '0006_branchnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='branchnews',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_branch', to='documents.Branch'),
        ),
    ]
