# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0011_auto_20160731_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='/mysite/static'),
        ),
    ]
