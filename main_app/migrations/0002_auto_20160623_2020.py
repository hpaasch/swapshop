# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 20:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 23, 20, 20, 41, 512084, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='location',
            field=models.CharField(choices=[('Denver', 'Denver'), ('SherrillsFord', 'SherrillsFord'), ('Mooresville', 'Mooresville'), ('Davidson', 'Davidson'), ('Cornelius', 'Cornelius'), ('Huntersville', 'Huntersville')], max_length=15),
        ),
    ]
