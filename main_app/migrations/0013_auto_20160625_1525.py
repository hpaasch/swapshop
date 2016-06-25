# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 15:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0012_auto_20160625_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='TraderProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.EmailField(blank=True, max_length=45)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo_images', verbose_name='Upload a logo')),
                ('preferred_city', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Listing')),
                ('primary_category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Category')),
                ('trader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='sellerprofile',
            name='preferred_city',
        ),
        migrations.RemoveField(
            model_name='sellerprofile',
            name='primary_category',
        ),
        migrations.RemoveField(
            model_name='sellerprofile',
            name='seller',
        ),
        migrations.DeleteModel(
            name='SellerProfile',
        ),
    ]