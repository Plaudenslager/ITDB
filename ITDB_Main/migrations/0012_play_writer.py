# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0011_auto_20150831_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='play',
            name='writer',
            field=models.ForeignKey(blank=True, to='ITDB_Main.People', null=True),
        ),
    ]
