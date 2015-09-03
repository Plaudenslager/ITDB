# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='play',
            name='synopsis',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='short_bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='play',
            name='year_written',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='theater',
            name='street_address',
            field=models.CharField(max_length=40, blank=True),
        ),
    ]
