# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-23 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0006_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodsid', models.IntegerField()),
                ('name', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('num', models.IntegerField()),
                ('orderid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myadmin.Orders')),
            ],
        ),
    ]
