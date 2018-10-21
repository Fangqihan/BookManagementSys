# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-20 23:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('birth_date', models.DateField()),
                ('gender', models.IntegerField(choices=[(0, 'male'), (1, 'female')], default=0)),
                ('email', models.EmailField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('pub_date', models.DateField()),
                ('word_count', models.IntegerField()),
                ('price', models.IntegerField(blank=True, null=True)),
                ('authors', models.ManyToManyField(to='book.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Publisher'),
        ),
    ]
