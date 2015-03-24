# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0012_auto_20150306_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 6, 17, 10, 14, 655000)),
            preserve_default=True,
        ),
    ]
