# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-01-03 07:06
from __future__ import unicode_literals

from django.db import migrations

def copy_order(apps, schema_editor):
    Category = apps.get_model('faqs', 'Category')
    for cat in Category.objects.all():
        cat.order = cat.ordering
        cat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0008_auto_20180102_2230'),
    ]

    operations = [
    ]
