# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-20 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zotero', '0006_auto_20161020_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zoteroattachment',
            name='attachment',
            field=models.FileField(blank=True, upload_to=b'zotero/'),
        ),
    ]
