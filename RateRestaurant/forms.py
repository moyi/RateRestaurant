
from django import forms
from django.contrib.auth.models import User
from RateRestaurant.models import Customer, Restaurant, Area, Comment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields=('username','password','email')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('telephone', 'picture')

class AreaForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="please enter the area name")
    slug = forms.SlugField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Area
        fields = ('name',)

class RestaurantForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    address = forms.CharField(max_length=128)
    telephone = forms.CharField(max_length=128)
    price = forms.IntegerField(initial=0)
    description = forms.CharField(widget=forms.Textarea)
    url = forms.URLField(max_length=200)
    slug = forms.SlugField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Restaurant
        exclude = ('slug','area','ave_rating')

class CommentForm(forms.ModelForm):
    rating = forms.FloatField(widget=forms.HiddenInput(),initial=0)
    food_rating = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'rating'}))
    service_rating =forms.FloatField(widget=forms.NumberInput(attrs={'class': 'rating'}))
    atmosphere_rating = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'rating'}))
    comments = forms.CharField(max_length=100000,widget=forms.Textarea)

    class Meta:
        model = Comment
        exclude = ('time','customer','restaurant','rating','likes')

class optionForm(forms.Form):
    OPTIONS = (
        ("rate","rating"),
        ("date","date")
    )
    option=forms.ChoiceField(choices=OPTIONS)