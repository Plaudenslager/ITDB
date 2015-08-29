# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0009_auto_20150822_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='headshot',
            field=models.ImageField(upload_to=b'photos', blank=True),
        ),
        migrations.AlterField(
            model_name='theater_pictures',
            name='image',
            field=models.ImageField(upload_to=b'photos', blank=True),
        ),
    ]
