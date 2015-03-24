# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0038_auto_20150316_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingrestaurant',
            name='restaurant',
        ),
        migrations.DeleteModel(
            name='RatingRestaurant',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='ave_rating',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='picture',
            field=models.ImageField(default=b'static/images/profile.jpg', upload_to=b'static/images', blank=True),
        ),
    ]
