# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-13 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football_data', '0004_auto_20170313_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='appmatch',
            name='coach_team_is_home_team',
            field=models.BooleanField(default=True),
        ),
    ]
