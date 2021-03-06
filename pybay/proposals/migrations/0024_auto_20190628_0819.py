# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2019-06-28 15:19
from __future__ import unicode_literals

from django.db import migrations

def forwards(apps, schema_editor):
    if schema_editor.connection.vendor != 'mysql':
        return
    schema_editor.execute("ALTER TABLE symposion_speakers_speaker CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    try:
        schema_editor.execute("ALTER TABLE proposals_tutorialproposal drop column what_will_attendees_learn")
    except Exception:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0023_auto_20190623_1648'),
    ]

    operations = [
        migrations.RunPython(forwards),
    ]
