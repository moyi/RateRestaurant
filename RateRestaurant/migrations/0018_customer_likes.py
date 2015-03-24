# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0017_comment_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
