# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-25 23:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0036_auto_20160325_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='franchise_name',
            new_name='franchise_blah',
        ),
    ]
