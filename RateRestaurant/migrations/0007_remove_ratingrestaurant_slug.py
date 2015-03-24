# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0006_ratingrestaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingrestaurant',
            name='slug',
        ),
    ]
