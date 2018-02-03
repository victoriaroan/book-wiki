# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-18 02:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('bsn', models.CharField(max_length=25, verbose_name='Short Name')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('content', markdownx.models.MarkdownxField(blank=True)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='projects.Book')),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psn', models.CharField(help_text='Used as the slug in URLs.', max_length=15, unique=True, verbose_name='Short Name')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('protected', models.BooleanField(default=False, editable=False)),
                ('index_page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='projects.Page')),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='projects.Project'),
        ),
        migrations.AddField(
            model_name='book',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='projects.Project'),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together=set([('bsn', 'project')]),
        ),
    ]
