from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect
from .models import CarOwner, Car
from .tables import carTable
from customer_page.forms import SetPasswordForm
from .forms import CarForm, ownerForm, CarEditForm
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
            if hasattr(user, 'customer'):
                return redirect('../../customer_page/customer_home')
            else:
                return redirect(index)
        else:
            messages.info(request, "Invalid password or username")
            return redirect(login_view)

    else:
        return render(request, 'owners_page/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def registration(request):
    form = ownerForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                email = form.cleaned_data['email']
                user = User.objects.create_user(username, email, password)
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
                carowner = CarOwner()
                carowner.car_owner = user
                carowner.mobile = form.cleaned_data['mobile']
                carowner.location = form.cleaned_data['location']

                carowner.save()
                return redirect(index)
            except:
                messages.info(request, "this username is already used")
                return redirect(registration)

    else:
        return render(request, 'owners_page/register.html', locals())


@login_required
def add_car(request):
    form = CarForm(request.POST or None)
    user = request.user
    if hasattr(user, 'carowner'):
        if request.method == 'POST':
            if form.is_valid():
                car = Car()
                car.car_name = form.cleaned_data['car_name']
                car.car_model = form.cleaned_data['car_model']
                car.car_seats = form.cleaned_data['car_seats']
                car.gearbox = form.cleaned_data['gearbox']
                car.price = form.cleaned_data['price']
                car.extra_info = form.cleaned_data['extra_info']
                car.owner = user.carowner
                car.save()
                return redirect(manage)
        else:
            return render(request, 'owners_page/car_added.html', {'form': form})
    else:
        message = "you are are a customer, you can't add a car"
        return render(request, 'owners_page/car_added.html', {'message': message})




@login_required
def edit_car(request, id):
    car = Car.objects.get(id=id)
    form = CarEditForm(request.POST or None, instance=car)
    user = request.user
    if hasattr(user, 'carowner'):
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect(manage)
        else:
            return render(request, 'owners_page/edit_car.html', {'form': form, 'id': id})
    else:
        message = "you are are a customer, you can't edit a car"
        return render(request, 'owners_page/edit_car.html', {'message': message})


@login_required
def delete_car(request, id):
    car = Car.objects.get(id=id)
    form = CarEditForm(request.POST or None, instance=car)
    user = request.user
    if hasattr(user, 'carowner'):
        car.delete()
        return redirect(manage)
    else:
        message = "you are are a customer, you can't edit a car"
        return render(request, 'owners_page/edit_car.html', {'message': message})


@login_required
def manage(request):
    user = request.user
    table = carTable(Car.objects.filter(owner__car_owner=user))

    return render(request, 'owners_page/manage.html', {'table': table})


@login_required
def password_change(request):
    user = request.user
    form = SetPasswordForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(logout_user)
    return render(request, 'owners_page/password_reset_confirm.html', {'form': form})