# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character', models.CharField(max_length=40)),
                ('billed_as', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('short_bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('year_written', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('production_company', models.CharField(max_length=100)),
                ('play', models.ForeignKey(to='ITDB_Main.Play')),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('street_address', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('state_or_province', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='production',
            name='theater',
            field=models.ForeignKey(to='ITDB_Main.Theater'),
        ),
        migrations.AddField(
            model_name='cast',
            name='person',
            field=models.ForeignKey(to='ITDB_Main.People'),
        ),
        migrations.AddField(
            model_name='cast',
            name='production',
            field=models.ForeignKey(to='ITDB_Main.Production'),
        ),
    ]
