# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20160623_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Watercraft', 'Watercraft'), ('Motor', 'Motor'), ('Sail', 'Sail'), ('Paddle', 'Paddle'), ('Gear', 'Gear'), ('Fishing', 'Fishing'), ('Recreation', 'Recreation'), ('Services', 'Services'), ('Land', 'Land'), ('Water', 'Water')], default=2, max_length=15),
            preserve_default=False,
        ),
    ]
