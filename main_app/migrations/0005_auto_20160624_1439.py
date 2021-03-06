# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_listing_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=30)),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Category')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='sub_category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='main_app.Category'),
            preserve_default=False,
        ),
    ]
