# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-03 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_auto_20180903_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='department_documents/'),
        ),
    ]
