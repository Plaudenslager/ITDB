# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0012_play_writer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musicians',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instrument', models.CharField(max_length=40)),
                ('person', models.ForeignKey(to='ITDB_Main.People')),
                ('production', models.ForeignKey(to='ITDB_Main.Production')),
            ],
        ),
    ]
