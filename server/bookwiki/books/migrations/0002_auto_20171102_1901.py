# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-02 23:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
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