# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0020_auto_20151011_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='headshot',
            field=models.ImageField(default=b'/photos/person_sillouette.png', upload_to=b'photos'),
        ),
    ]
