# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0006_auto_20150820_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job', models.CharField(max_length=40)),
                ('is_director', models.BooleanField(default=False)),
                ('is_writer', models.BooleanField(default=False)),
                ('is_producer', models.BooleanField(default=False)),
                ('person', models.ForeignKey(to='ITDB_Main.People')),
                ('production', models.ForeignKey(to='ITDB_Main.Production')),
            ],
        ),
        migrations.RemoveField(
            model_name='cast',
            name='is_director',
        ),
        migrations.RemoveField(
            model_name='cast',
            name='is_producer',
        ),
        migrations.RemoveField(
            model_name='cast',
            name='is_writer',
        ),
    ]
