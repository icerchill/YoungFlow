# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 00:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0004_auto_20160801_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='alias',
            field=models.CharField(default=datetime.datetime(2016, 8, 2, 0, 17, 30, 585000, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=datetime.datetime(2016, 8, 2, 0, 17, 42, 257000, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=datetime.datetime(2016, 8, 2, 0, 17, 52, 38000, tzinfo=utc), max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='cellNumber',
            field=models.CharField(blank=True, default=datetime.datetime(2016, 8, 2, 0, 18, 5, 892000, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
    ]