# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 23:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_auto_20160625_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traderprofile',
            name='email_address',
            field=models.EmailField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='traderprofile',
            name='preferred_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Location'),
        ),
        migrations.AlterField(
            model_name='traderprofile',
            name='primary_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Category'),
        ),
    ]