# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20160731_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='static'),
        ),
    ]
