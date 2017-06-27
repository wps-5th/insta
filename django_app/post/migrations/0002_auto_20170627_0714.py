# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 07:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video_ori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube_id', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('url_thumbnail', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.Video'),
        ),
    ]
