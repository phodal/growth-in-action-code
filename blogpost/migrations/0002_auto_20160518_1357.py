# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-18 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
