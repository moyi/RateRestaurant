# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0027_auto_20150313_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='picture',
            new_name='image',
        ),
    ]
