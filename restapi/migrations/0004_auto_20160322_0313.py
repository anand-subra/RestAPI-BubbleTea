# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-22 03:13
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0003_auto_20160322_0236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_written', models.DateTimeField(auto_now_add=True)),
                ('heading', models.CharField(max_length=30)),
                ('body', models.CharField(max_length=250)),
                ('rating', models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(150), django.core.validators.MinValueValidator(0)])),
                ('user_type', models.CharField(max_length=15)),
                ('location', models.CharField(blank=True, max_length=25)),
            ],
        ),
        migrations.RenameField(
            model_name='film',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='film',
            name='rating',
        ),
        migrations.AddField(
            model_name='film',
            name='actors',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='film',
            name='composer',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='film',
            name='director',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
