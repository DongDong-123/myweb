# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-10 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.IntegerField()),
                ('goods', models.CharField(max_length=32)),
                ('company', models.CharField(max_length=50)),
                ('descr', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('picname', models.CharField(max_length=255)),
                ('state', models.IntegerField(default=1, max_length=1)),
                ('store', models.IntegerField(default=0)),
                ('num', models.IntegerField(default=0)),
                ('clicknum', models.IntegerField(default=0)),
                ('addtime', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('linkman', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=6)),
                ('phone', models.CharField(max_length=16)),
                ('addtime', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('pid', models.IntegerField(default=0)),
                ('path', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('name', models.CharField(max_length=16, null=True)),
                ('password', models.CharField(max_length=32)),
                ('sex', models.IntegerField(max_length=1, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('code', models.CharField(max_length=6, null=True)),
                ('phone', models.CharField(max_length=16, null=True)),
                ('email', models.CharField(max_length=50)),
                ('state', models.IntegerField(max_length=1, null=True)),
                ('addtime', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='detail',
            name='orderid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myadmin.Orders'),
        ),
    ]
