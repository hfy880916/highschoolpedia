# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-28 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_article_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='atribute',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
