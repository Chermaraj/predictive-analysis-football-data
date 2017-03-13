# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-12 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('football_data', '0002_auto_20170312_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('home_team', models.CharField(max_length=30)),
                ('away_team', models.CharField(max_length=30)),
                ('full_time_home_goals', models.PositiveSmallIntegerField()),
                ('full_time_away_goals', models.PositiveSmallIntegerField()),
                ('half_time_home_goals', models.PositiveSmallIntegerField()),
                ('half_time_away_goals', models.PositiveSmallIntegerField()),
                ('home_possession', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('away_possession', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('home_total_shots', models.PositiveSmallIntegerField()),
                ('away_total_shots', models.PositiveSmallIntegerField()),
                ('home_shots_on_target', models.PositiveSmallIntegerField()),
                ('away_shots_on_target', models.PositiveSmallIntegerField()),
                ('home_corners', models.PositiveSmallIntegerField()),
                ('away_corners', models.PositiveSmallIntegerField()),
                ('home_fouls_committed', models.PositiveSmallIntegerField()),
                ('away_fouls_committed', models.PositiveSmallIntegerField()),
                ('home_yellow_cards', models.PositiveSmallIntegerField()),
                ('away_yellow_cards', models.PositiveSmallIntegerField()),
                ('home_red_cards', models.PositiveSmallIntegerField()),
                ('away_red_cards', models.PositiveSmallIntegerField()),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='football_data.Coach')),
            ],
            options={
                'verbose_name_plural': 'Matches',
            },
        ),
    ]