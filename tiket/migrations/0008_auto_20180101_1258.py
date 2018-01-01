# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-01 12:58
from __future__ import unicode_literals

from django.db import migrations, models
import tiket.models


class Migration(migrations.Migration):

    dependencies = [
        ('tiket', '0007_auto_20180101_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tiket',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='tiket',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='tiket',
            name='bukti_pembayaran',
            field=models.ImageField(blank=True, null=True, upload_to=tiket.models.upload_location),
        ),
    ]