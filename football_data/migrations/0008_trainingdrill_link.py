# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-04 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football_data', '0007_auto_20170404_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingdrill',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
