# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-06 15:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0003_auto_20180806_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweet_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 6, 15, 16, 21, 143800, tzinfo=utc)),
        ),
    ]
