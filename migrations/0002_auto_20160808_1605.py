# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 16:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zotero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zoteroreference',
            name='fetch_timestamp',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 8, 8, 16, 5, 33, 819718)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='zoteroreference',
            name='key',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
