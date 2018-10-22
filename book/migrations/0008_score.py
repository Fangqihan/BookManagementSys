# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-22 00:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0001_initial'),
        ('book', '0007_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='my_auth.UserInfo')),
            ],
        ),
    ]
