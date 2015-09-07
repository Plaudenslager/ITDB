# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITDB_Main', '0016_auto_20150906_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Production_Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('sponsor', models.BooleanField(default=False)),
                ('link', models.URLField()),
                ('image', models.ImageField(upload_to=b'', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='production',
            name='production_company',
        ),
        migrations.AddField(
            model_name='production',
            name='prod_company',
            field=models.ForeignKey(to='ITDB_Main.Production_Company', null=True),
        ),
    ]
