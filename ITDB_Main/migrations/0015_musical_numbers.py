# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0014_auto_20150906_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musical_Numbers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('composer', models.ForeignKey(blank=True, to='ITDB_Main.People', null=True)),
                ('play', models.ForeignKey(to='ITDB_Main.Play')),
            ],
        ),
    ]
