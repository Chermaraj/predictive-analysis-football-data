# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football_data', '0012_player_has_played_match'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='away_win_average_odds',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='away_win_max_odds',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='home_draw_average_odds',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='home_draw_max_odds',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='home_win_average_odds',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='home_win_max_odds',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
