# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-27 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('football_data', '0016_merge_20170225_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineLearningModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algorithm', models.CharField(choices=[('LogisticRegression', 'LogisticRegression'), ('GradientBoosting', 'LogisticRegression')], max_length=50)),
                ('training_data', models.FileField(upload_to='None/training_data')),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='machinelearningmodel',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='football_data.Sport'),
        ),
    ]
