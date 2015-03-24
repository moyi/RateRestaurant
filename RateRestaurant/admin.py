from django.contrib import admin
from RateRestaurant.models import Customer,Restaurant,Area,Comment, Like

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user','telephone','picture','likes')

class RestaurantAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name','area')}
    list_display = ('name','ave_rating','address','telephone','price','area','description','image')

class AreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('customer','restaurant','comments','rating','time','likes')


class LikeAdmin(admin.ModelAdmin):
    list_display = ('comment','customer')

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Area,AreaAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Like,LikeAdmin)

