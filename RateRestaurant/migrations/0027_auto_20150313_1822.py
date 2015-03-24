# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0026_auto_20150313_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='picture',
            field=models.ImageField(upload_to=b'profile_images', blank=True),
        ),
    ]
