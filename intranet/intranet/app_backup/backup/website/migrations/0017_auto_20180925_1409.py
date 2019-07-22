# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-25 14:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0016_auto_20180925_0546'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_title', models.CharField(blank=True, max_length=255, null=True)),
                ('file_type', models.CharField(blank=True, max_length=255, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='event_files/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Event Files',
            },
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_image',
        ),
        migrations.AddField(
            model_name='event',
            name='event_end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='eventfile',
            name='file_post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='branch_news_file', to='website.Event'),
        ),
        migrations.AddField(
            model_name='eventfile',
            name='posted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
