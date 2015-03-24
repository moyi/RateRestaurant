# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0031_auto_20150313_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='slug',
            field=models.SlugField(),
        ),
    ]
