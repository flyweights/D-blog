# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-05 06:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20180105_1408'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commment',
            new_name='Comment',
        ),
    ]
