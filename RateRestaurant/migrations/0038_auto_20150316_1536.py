# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0037_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='picture',
            field=models.ImageField(upload_to=b'static/images', blank=True),
        ),
    ]
