# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-27 12:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180926_0729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogfile',
            name='file_post',
        ),
        migrations.RemoveField(
            model_name='blogfile',
            name='posted_by',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_by',
        ),
        migrations.DeleteModel(
            name='BlogFile',
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
