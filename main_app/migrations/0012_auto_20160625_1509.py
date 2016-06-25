# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 15:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0011_auto_20160624_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.EmailField(max_length=45)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo_images', verbose_name='Upload a logo')),
            ],
        ),
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='sellerprofile',
            name='preferred_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Listing'),
        ),
        migrations.AddField(
            model_name='sellerprofile',
            name='primary_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Category'),
        ),
        migrations.AddField(
            model_name='sellerprofile',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
