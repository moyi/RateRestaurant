# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0040_auto_20150320_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='picture',
            field=models.ImageField(default=b'static/images/profile.jpg', upload_to=b'static/images', blank=True),
        ),
    ]
