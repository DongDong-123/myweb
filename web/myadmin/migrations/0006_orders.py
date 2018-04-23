# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-23 01:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0005_auto_20180413_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkman', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=6)),
                ('phone', models.CharField(max_length=16)),
                ('addtime', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('nums', models.ImageField(default=1, upload_to='')),
                ('status', models.IntegerField(default=0)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.Users')),
            ],
        ),
    ]
