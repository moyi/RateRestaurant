# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateRestaurant', '0036_auto_20150314_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.ForeignKey(to='RateRestaurant.Comment')),
                ('customer', models.ForeignKey(to='RateRestaurant.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
