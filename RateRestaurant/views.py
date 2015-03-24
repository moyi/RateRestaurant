from django.shortcuts import render
from RateRestaurant.models import Customer,Restaurant,Area,Comment,Like
from RateRestaurant.forms import UserForm,CustomerForm, AreaForm,RestaurantForm, CommentForm, optionForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime

def overRate():
    restaurant_list = Restaurant.objects.all()
    for res in restaurant_list:
        comment_rating = Comment.objects.filter(restaurant=res)
        count = 0
        rating = 0
        for rat in comment_rating:
            count += 1
            rating += rat.rating
        if count!=0:
            rating /= count
            rating = round(rating,1)
        res.ave_rating = rating
        res.save()


def updateCustomer():
    customer = Customer.objects.all()
    for cus in customer:
        comment_like = Comment.objects.filter(customer = cus)
        likes = 0
        for like in comment_like:
            likes += like.likes
        cuss = Customer.objects.get(user = cus.user)
        cuss.likes = likes
        cuss.save()


def home(request):
    area_list = Area.objects.all()
    overRate()
    top=Restaurant.objects.order_by('-ave_rating')[:5]
    updateCustomer()
    customer = Customer.objects.order_by('-likes')
    context_list={}
    context_list['area'] = area_list
    context_list['restaurant'] = top
    context_list['customer'] = customer
    return render(request, 'RateRestaurant/homePage.html', context_list)

def area(request,area_name_slug):
    context_dict = {}
    try:
        area = Area.objects.get(slug=area_name_slug)
        context_dict['area_name'] = area.name
        restaurant = Restaurant.objects.filter(area=area)
        context_dict['area'] = area
        context_dict['area_all']=Area.objects.all()
        context_dict['restaurant'] = restaurant
    except area.DoesNotExist:
        pass
    # Go render the response and return it to the client.
    return render(request, 'RateRestaurant/Area.html', context_dict)

def restaurant(request,restaurant_name_slug):
    context_dict = {}
    try:
        restaurant = Restaurant.objects.get(slug = restaurant_name_slug)
        context_dict['area_all']=Area.objects.all()
        context_dict['restaurant'] = restaurant
        context_dict['restaurant_name'] = restaurant.name
        res_comment = Comment.objects.filter(restaurant = restaurant)
        context_dict['comment'] = res_comment.order_by('-time')
        if request.method=='POST':
            opt=request.POST.get('dropdown','rate')
            if opt=='rate':
                context_dict['comment'] = res_comment.order_by('-rating')
                context_dict['option']='rate'

        context_dict['rate']=restaurant.ave_rating
    except restaurant.DoesNotExist:
        pass
    return render(request,'RateRestaurant/Restaurant.html',context_dict)

@login_required
def like_comment(request):
    global current_user
    com_id = None
    if request.method == 'GET':
        com_id = request.GET['comment_id']
        current_user = Customer.objects.get(user = request.user)
    if com_id:
        com = Comment.objects.get(id=int(com_id))
        like = Like.objects.filter(customer = current_user,comment=com)
        if  com and not like:
            a = Like(customer = current_user,comment=com)
            a.save()
            likes = com.likes + 1
            com.likes =  likes
            com.save()
            return HttpResponse(likes)

def check_like(current_user,comment):
    like = Like.objects.get(customer = current_user,comment=comment)
    if like:
        return False
    else:

        return True


def add_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print form.errors
    else:
        form=AreaForm()
    return render(request,'RateRestaurant/AddArea.html', {'form': form})

def add_restaurant(request,area_name_slug):
    try:
        a = Area.objects.get(slug=area_name_slug)
    except Area.DoesNotExist:
        a = None
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            if a:
                restaurant = form.save(commit=False)
                restaurant.area = a
                restaurant.image = request.FILES['image']
                restaurant.save()
                overRate()
                return area(request,area_name_slug)
        else:
            print form.errors
    else:
        form=RestaurantForm()
    return render(request,'RateRestaurant/AddRestaurant.html', {'form': form,'area':a})

def add_comment(request,restaurant_name_slug):
    try:
        rest = Restaurant.objects.get(slug = restaurant_name_slug)
    except Restaurant.DoesNotExist:
        rest = None

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if rest:
                comment = form.save(commit=False)
                comment.restaurant = rest
                comment.customer = Customer.objects.get(user = request.user)
                comment.rating = round((comment.food_rating + comment.service_rating + comment.atmosphere_rating) / 3,1)
                comment.time=datetime.now()
                comment.save()
                overRate()
                return restaurant(request,restaurant_name_slug)
        else:
            print form.errors
    else:
        form = CommentForm()
    return render(request,'RateRestaurant/addComment.html',{'form':form,'restaurant':rest})

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        customer_form = CustomerForm(data = request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save();
            user.set_password(user.password)
            user.save()
            customer = customer_form.save(commit = False)
            customer.user = user
            if 'picture' in request.FILES:
                customer.picture = request.FILES['picture']
            customer.save()
            registered = True
        else:
            print user_form.errors, customer_form.errors
    else:
        user_form = UserForm()
        customer_form = CustomerForm()

    return render(request,'RateRestaurant/register.html',{'user_form': user_form, 'customer_form':customer_form,
                                                          'registered': registered})

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/RateRestaurant/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Restaurant account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'RateRestaurant/login.html', {})

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/RateRestaurant/')

