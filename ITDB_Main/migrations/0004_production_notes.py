# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0003_auto_20150820_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
