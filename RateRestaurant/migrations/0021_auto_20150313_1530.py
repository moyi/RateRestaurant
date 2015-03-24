# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0020_auto_20150312_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='description',
            field=models.CharField(default=b'', max_length=1000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='picture',
            field=models.ImageField(default=datetime.date(2015, 3, 13), upload_to=b'profile_images', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(default=b'', unique=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(default=b'', max_length=128),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='telephone',
            field=models.CharField(default=b'', max_length=128),
        ),
    ]
