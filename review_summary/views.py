from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
from tablib import Dataset
from .models import Restaurant, Review
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm



def simple_upload(request):
    if request.method == 'POST':
        person_resource = RestaurantResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

def index_page(request):
    return render(request, 'restaurant/intro.html', {})

def get_restaurants(request):
    query = request.GET.get('search')
    locality = request.GET.get('locality')

    # , restaurantLocation=locality
    if locality == None:
        rest = Restaurant.objects.filter(restaurantCity__icontains=query)
    else:
        rest = Restaurant.objects.filter(restaurantCity__icontains=query, restaurantLocation__icontains=locality)

    paginator = Paginator(rest, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    rest = paginator.get_page(page)
    return render(request, 'restaurant/restaurant.html', {'restaurants': rest, 'query': query})


def restaurant_list(request):
    rest = Restaurant.objects.all()
    return render(request, 'restaurant/restaurants.html', {'restaurants': rest})

def restaurant_detail(request, id):
    rest = get_object_or_404(Restaurant, id=id)
    review = Review.objects.filter(rest_id=id)
    # rest = Restaurant.objects.all()
    return render(request, 'restaurant/restaurant_detail.html', {'restaurant': rest, 'reviews': review})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'mysite/register.html', {'form' : form})
