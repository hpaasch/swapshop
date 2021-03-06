# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_auto_20160625_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='traderprofile',
            old_name='contact',
            new_name='email_address',
        ),
        migrations.AlterField(
            model_name='traderprofile',
            name='preferred_location',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Location'),
        ),
    ]
