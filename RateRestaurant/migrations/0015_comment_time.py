# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0014_remove_comment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 6, 20, 18, 14, 114000)),
            preserve_default=True,
        ),
    ]
