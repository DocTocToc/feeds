# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0009_add_category_to_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='logo',
            field=models.URLField(blank=True, null=True, verbose_name='logo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='categories', to='category.Category'),
        ),
    ]