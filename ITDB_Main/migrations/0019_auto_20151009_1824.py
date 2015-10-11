# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0018_auto_20150907_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='play',
            name='play_type',
            field=models.CharField(blank=True, max_length=2, choices=[(b'S', b'Straight Play'), (b'M', b'Musical'), (b'O', b'Opera')]),
        ),
        migrations.AddField(
            model_name='theater',
            name='seating_capacity',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
