# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-20 12:56
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zotero', '0003_zoteroattachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zoteroattachment',
            name='attachment',
            field=models.FileField(blank=True, storage=django.core.files.storage.FileSystemStorage(location=b'/media/photos'), upload_to=b''),
        ),
    ]
