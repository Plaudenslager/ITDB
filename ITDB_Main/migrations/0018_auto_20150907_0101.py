# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0017_auto_20150907_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production_company',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
