# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 01:00
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20171108_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='content',
            field=markdownx.models.MarkdownxField(blank=True),
        ),
    ]
