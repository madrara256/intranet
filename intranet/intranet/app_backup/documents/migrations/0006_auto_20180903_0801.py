# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-03 08:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_auto_20180903_0751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='category',
            new_name='document_category',
        ),
    ]
