# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-22 01:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_auto_20181022_0840'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]