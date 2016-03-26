# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-22 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0016_auto_20160322_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='film_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film', to='restapi.Film'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to='restapi.User'),
        ),
    ]