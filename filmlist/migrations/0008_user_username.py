# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-22 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmlist', '0007_remove_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=34234, max_length=40),
            preserve_default=False,
        ),
    ]
