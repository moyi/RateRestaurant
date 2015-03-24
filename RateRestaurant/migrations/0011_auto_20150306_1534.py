# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0010_auto_20150306_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingrestaurant',
            name='restaurant',
            field=models.ForeignKey(to='RateRestaurant.Restaurant'),
        ),
    ]
