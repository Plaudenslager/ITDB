# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0010_auto_20150822_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='cast',
            name='end_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cast',
            name='is_alternating',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cast',
            name='is_understudy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cast',
            name='start_year',
            field=models.IntegerField(default=0),
        ),
    ]
