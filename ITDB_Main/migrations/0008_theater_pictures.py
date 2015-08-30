# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0007_auto_20150820_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theater_pictures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('theater', models.ForeignKey(to='ITDB_Main.Theater')),
            ],
        ),
    ]
