# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-20 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0005_auto_20180413_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='addtime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
