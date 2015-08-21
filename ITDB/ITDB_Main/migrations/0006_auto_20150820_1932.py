# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0005_auto_20150820_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theater',
            name='city',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='theater',
            name='state_or_province',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
