# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-12 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='clicknum',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='company',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='descr',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='picname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='typeid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.Type'),
        ),
    ]
