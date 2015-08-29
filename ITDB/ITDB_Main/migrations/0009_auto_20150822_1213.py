# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0008_theater_pictures'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='play',
            name='year_written',
        ),
        migrations.AddField(
            model_name='people',
            name='headshot',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
