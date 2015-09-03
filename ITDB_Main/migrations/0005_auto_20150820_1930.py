# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0004_production_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theater',
            name='city',
            field=models.CharField(max_length=40, blank=True),
        ),
    ]
