# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 14:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_unique_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='feeds.Post')),
                ('was_announced', models.BooleanField(default=False)),
                ('was_recommended', models.BooleanField(default=False)),
                ('updated_social', models.DateTimeField(blank=True, default=False, null=True)),
                ('tweets', models.IntegerField(default=0)),
                ('blogs', models.IntegerField(default=0)),
                ('plus1', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('linkedin', models.IntegerField(default=0)),
                ('shares', models.IntegerField(default=0)),
                ('pageviews', models.IntegerField(default=0)),
                ('sentiment', models.FloatField()),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='blogs',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pageviews',
        ),
        migrations.RemoveField(
            model_name='post',
            name='plus1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='score',
        ),
        migrations.RemoveField(
            model_name='post',
            name='shares',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tweets',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_social',
        ),
        migrations.RemoveField(
            model_name='post',
            name='was_announced',
        ),
        migrations.RemoveField(
            model_name='post',
            name='was_recommended',
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='feeds.Category'),
        ),
        migrations.AlterField(
            model_name='enclosure',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='enclosure', to='feeds.Post'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='website',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='feeds', to='feeds.WebSite'),
        ),
        migrations.AlterField(
            model_name='feedentrystats',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='feeds.Feed'),
        ),
        migrations.AlterField(
            model_name='feedpostcount',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='feeds.Feed', verbose_name='feed'),
        ),
        migrations.AlterField(
            model_name='options',
            name='user',
            field=models.ForeignKey(help_text='User', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='posts', to='feeds.Feed', verbose_name='feed'),
        ),
        migrations.AlterField(
            model_name='post',
            name='has_errors',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='postreadcount',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='feeds.Post'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='feed_subscription', to='feeds.Feed', verbose_name='Feed Subscription'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_subscription', to='feeds.Options', verbose_name='User Subscription'),
        ),
        migrations.AlterField(
            model_name='taggedpost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='feeds.Post', verbose_name='post'),
        ),
        migrations.AlterField(
            model_name='taggedpost',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='post_tags', to='feeds.Tag', verbose_name='tag'),
        ),
    ]