# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-24 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0009_auto_20180423_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turnimg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='static/public/front/public/img')),
            ],
        ),
    ]