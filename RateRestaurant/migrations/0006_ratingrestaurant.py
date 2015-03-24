# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0005_auto_20150305_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingRestaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ave_rating', models.FloatField(default=0.0)),
                ('slug', models.SlugField()),
                ('restaurant', models.ForeignKey(to='RateRestaurant.Restaurant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
