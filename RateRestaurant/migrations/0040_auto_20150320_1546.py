# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0039_auto_20150320_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='picture',
            field=models.ImageField(default=b'static/images/profile.jpg', upload_to=b'static/images', width_field=100, height_field=100, blank=True),
        ),
    ]
