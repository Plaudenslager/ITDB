# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0021_auto_20151011_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='first_name',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='people',
            name='last_name',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
