# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20160625_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traderprofile',
            name='preferred_city',
        ),
        migrations.AddField(
            model_name='traderprofile',
            name='preferred_location',
            field=models.CharField(choices=[('Denver', 'Denver'), ('SherrillsFord', 'SherrillsFord'), ('Mooresville', 'Mooresville'), ('Davidson', 'Davidson'), ('Cornelius', 'Cornelius'), ('Huntersville', 'Huntersville')], default=2, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='location',
            field=models.CharField(choices=[('Denver', 'Denver'), ('SherrillsFord', 'SherrillsFord'), ('Mooresville', 'Mooresville'), ('Davidson', 'Davidson'), ('Cornelius', 'Cornelius'), ('Huntersville', 'Huntersville')], max_length=15),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]