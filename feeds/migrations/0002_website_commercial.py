# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='commercial',
            field=models.BooleanField(default=True),
        ),
    ]