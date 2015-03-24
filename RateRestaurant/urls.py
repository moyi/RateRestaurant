__author__ = 'chen'
from django.conf.urls import patterns, url
from RateRestaurant import views

urlpatterns = patterns('',
    url(r'^$',views.home,name='home'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^area/(?P<area_name_slug>[\w\-]+)/$', views.area, name='area'),
    url(r'^restaurant/(?P<restaurant_name_slug>[\w\-]+)/$',views.restaurant, name='restaurant'),
    url(r'^add_restaurant/(?P<area_name_slug>[\w\-]+)/$', views.add_restaurant, name='add_restaurant'),
    url(r'^add_area/$', views.add_area, name='add_area'),
    url(r'^add_comment/(?P<restaurant_name_slug>[\w\-]+)/$',views.add_comment, name='add_comment'),
    url(r'^like_comment/$', views.like_comment, name='like_comment'),

                       )
