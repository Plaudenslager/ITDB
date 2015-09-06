# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0015_musical_numbers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musical_Number',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('composer', models.ForeignKey(blank=True, to='ITDB_Main.People', null=True)),
                ('play', models.ForeignKey(to='ITDB_Main.Play')),
            ],
        ),
        migrations.RemoveField(
            model_name='musical_numbers',
            name='composer',
        ),
        migrations.RemoveField(
            model_name='musical_numbers',
            name='play',
        ),
        migrations.DeleteModel(
            name='Musical_Numbers',
        ),
    ]
