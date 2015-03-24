# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0004_auto_20150305_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='atmosphere_rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='food_rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='service_rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
