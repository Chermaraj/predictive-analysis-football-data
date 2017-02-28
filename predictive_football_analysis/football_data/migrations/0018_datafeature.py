# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-27 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('football_data', '0017_auto_20170227_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('is_target_feature', models.BooleanField(default=False)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='football_data.MachineLearningModel')),
            ],
        ),
    ]
