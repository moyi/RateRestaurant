# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0033_auto_20150313_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='atmosphere_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='food_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='service_rating',
            field=models.FloatField(default=0),
        ),
    ]
