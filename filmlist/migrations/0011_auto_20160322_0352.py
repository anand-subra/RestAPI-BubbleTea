# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-22 03:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmlist', '0010_auto_20160322_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='review',
            name='film_name',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, related_name='review_film_name', to='filmlist.Film'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='writer',
            field=models.ForeignKey(default=456, on_delete=django.db.models.deletion.CASCADE, related_name='review_writter', to='filmlist.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]