# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-24 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_advice'),
    ]

    operations = [
        migrations.CreateModel(
            name='data_c',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=20)),
                ('level', models.CharField(max_length=20)),
                ('disease', models.CharField(max_length=20)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
