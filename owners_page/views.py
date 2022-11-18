from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect
from .models import CarOwner, Car
# Create your views here.
from owners_page.models import CarOwner, Car


def index(request):
    """home page for the owners page"""
    if not request.user.is_authenticated:
        return render(request, 'owners_page/login.html')
    else:
        return render(request, 'owners_page/owner_home.html')


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/owner_home')
        else:
            messages.info(request, "Invalid password or username")
            return redirect('login')

    else:
        return render(request, 'owners_page/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')

def registration(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        mobile = request.POST['mobile']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        city = request.POST['city']
        city = city.lower()
        postcode = request.POST['postcode']

        try:
            user = User.objects.create_user(username = username, email = email)
            user.first_name = firstname
            user.last_name = lastname
            user.set_password(password)
            user.save()
            messages.info(request, "Registration successful, now you can register your car.")
            return redirect('login-view')
        except:
            messages.info(request, "username already exists")
            return render(request, 'owners_page/register.html')

    else:
        return render(request, 'owners_page/register.html')
@login_required
def add_car(request):
    car_name = request.POST['car_name']
    city = request.POST['city']
    city = city.lower()
    postcode = request.POST['postcode']
    description = request.POST['description']
    capacity = request.POST['capacity']

    locaiton = request.POST['location']
    phone = request.POST['phone']
    wallet = request.POST['wallet']

    car_owner_obj = CarOwner.objects.create(
        car_owner =request.user,
        location = locaiton,
        wallet = wallet,
        mobile = phone
    )
    car_owner_obj.save()
    car = Car(car_name=car_name, owner=car_owner_obj, description=description, capacity=capacity)
    car.save()
    # try:
    #     location = CarOwner.objects.get(city = city, postcode = postcode)
    # except:
    #     location = None
    # if location is not None:
    #     car = Car(car_name=car_name, color=color, dealer=cd, location = location, description = description, capacity=capacity)
    # else:
    #     location = CarOwner(city = city, postcode = postcode)
    #     location.save()
    #     location = CarOwner.objects.get(city = city, postcode = postcode)
    #     car = Car(car_name=car_name, color=color, dealer=cd, location = location,description=description, capacity=capacity)
    # car.save()
    return render(request, 'owners_page/car_added.html')