# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-28 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football_data', '0028_auto_20170228_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='datafeature',
            name='mean',
            field=models.FloatField(default=0),
        ),
    ]