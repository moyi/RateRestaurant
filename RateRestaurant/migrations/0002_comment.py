# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(max_length=5)),
                ('comments', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('customer', models.ForeignKey(to='RateRestaurant.Customer')),
                ('restaurant', models.ForeignKey(to='RateRestaurant.Restaurant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
