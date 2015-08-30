# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0002_auto_20150820_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='cast',
            name='is_director',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cast',
            name='is_producer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cast',
            name='is_writer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cast',
            name='billed_as',
            field=models.CharField(max_length=40, blank=True),
        ),
    ]
