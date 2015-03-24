from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from PIL import Image
from datetime import datetime

class Customer(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    telephone = models.CharField(max_length=128,blank=True)
    picture = models.ImageField(upload_to='static/images', default='static/images/profile.jpg', blank=True)
    likes=models.IntegerField(default=0)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Area(models.Model):
    name = models.CharField(max_length=128,primary_key=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Area, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(default= '',max_length=128)
    address = models.CharField(default= '',max_length=128,unique=True)
    telephone = models.CharField(default= '',max_length=128)
    price = models.IntegerField(default=0)
    area = models.ForeignKey(Area)
    description = models.CharField(default= '',max_length=1000)
    image = models.ImageField(upload_to='static/images', blank=True)
    url = models.URLField()
    ave_rating = models.FloatField(default=0.0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
                self.slug = slugify(self.name+self.area.name)
                super(Restaurant, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

class Comment(models.Model):
    customer = models.ForeignKey(Customer)
    restaurant = models.ForeignKey(Restaurant)
    rating = models.FloatField(default=0)
    food_rating = models.FloatField(default=0)
    service_rating = models.FloatField(default=0)
    atmosphere_rating = models.FloatField(default=0)
    comments = models.CharField(max_length=100000)
    time = models.DateTimeField(null=True)
    likes=models.IntegerField(default=0)

    def __unicode__(self):
        return (str)(self.id)


class Like(models.Model):
    comment = models.ForeignKey(Comment)
    customer = models.ForeignKey(Customer)

    def __unicode__(self):
        return self.customer.user.username

