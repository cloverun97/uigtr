# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-01 04:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tiket.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nama', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('asal_sekolah', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Tiket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_pembayaran', models.CharField(choices=[('0', 'Belum lunas'), ('1', 'Menunggu konfirmasi'), ('2', 'Lunas'), ('3', 'Ditolak')], max_length=1)),
                ('jumlah_tiket_ipa', models.IntegerField(default=0)),
                ('jumlah_tiket_ips', models.IntegerField(default=0)),
                ('lokasi_TO', models.CharField(choices=[('0', 'Pekanbaru'), ('1', 'Bangkinang'), ('2', 'Duri'), ('3', 'Dumai'), ('4', 'Pangkalan Kerinci')], max_length=1)),
                ('bukti_pembayaran', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=tiket.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(blank=True, default=0)),
                ('width_field', models.IntegerField(blank=True, default=0)),
                ('created_time', models.DateTimeField()),
                ('time_remaining', models.DateTimeField()),
                ('siswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tikets', to='tiket.Siswa')),
            ],
            options={
                'ordering': ['-created_time', '-status_pembayaran'],
            },
        ),
    ]