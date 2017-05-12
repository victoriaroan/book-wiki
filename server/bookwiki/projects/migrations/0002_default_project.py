# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

def forwards_func(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    db_alias = schema_editor.connection.alias
    Project.objects.using(db_alias).create(id=1, name='Default Project', slug='default', protected=True)

def reverse_func(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    db_alias = schema_editor.connect.alias
    Project.objects.using(db_alias).filter(id=1).delete()

class Migration(migrations.Migration):
    
    dependencies = [
        ('projects', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
