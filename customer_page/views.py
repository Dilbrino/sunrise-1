from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import request
from django.shortcuts import render, redirect
from customer_page.models import Orders
from .forms import customerForm, SetPasswordForm, filter
from .models import Customer
from .tables import OrdersTable, carsTable
from owners_page.models import Car
from django_tables2 import RequestConfig


# Create your views here.
def index(request):
    """home page for the owners page"""
    if not request.user.is_authenticated:
        return render(request, 'customer_page/login.html')
    else:
        return render(request, 'customer_page/customer_home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            if hasattr(user, 'carowner'):
                return redirect('../../owners_page/owner_home')
            else:
                return redirect(index)
        else:
            messages.info(request, "Invalid password or username")
            return redirect(login)

    else:
        return render(request, 'customer_page/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def registration(request):
    form = customerForm(request.POST or None)
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
                customer = Customer()
                customer.user = user
                customer.mobile = form.cleaned_data['mobile']
                customer.location = form.cleaned_data['location']

                customer.save()
                return redirect(index)
            except:
                messages.info(request, "this username is already used")
                return redirect(registration)

    else:
        return render(request, 'customer_page/register.html', locals())


@login_required
def manage(request):
    # order_list = []
    user = request.user
    table = OrdersTable(Orders.objects.filter(user=user))

    return render(request, 'customer_page/manage.html', {'table': table})


@login_required
def password_change(request):
    user = request.user
    form = SetPasswordForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(logout_user)
    return render(request, 'customer_page/password_reset_confirm.html', {'form': form})


@login_required
def giveBack_car(request, id):
    order = Orders.objects.get(id=id)
    order.car.available_car = True
    order.car.save()
    order.is_complete = True
    order.save()
    return redirect(manage)


@login_required
def rent_car(request, id):
    car = Car.objects.get(id=id)
    car.available_car = False
    car.save()
    order = Orders()
    order.user = request.user
    order.car_owner = car.owner
    order.rent = 'rent'
    order.car = car
    order.days = 'abc'
    order.is_complete = False

    order.save()
    return redirect(manage)


@login_required
def search_car(request):
    query = Car.objects.filter(available_car=True)
    form = filter(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            if form.cleaned_data['name']:
                query = query.filter(car_name=form.cleaned_data['name'])
            if form.cleaned_data['model']:
                query = query.filter(car_model=form.cleaned_data['model'])
            if form.cleaned_data['seats']:
                query = query.filter(car_seats=form.cleaned_data['seats'])
            if form.cleaned_data['gearBox']:
                query = query.filter(gearbox=form.cleaned_data['gearBox'])
            if form.cleaned_data['location']:
                query = query.filter(owner__location=form.cleaned_data['location'])
    table = carsTable(query)
    RequestConfig(request).configure(table)
    return render(request, 'customer_page/search.html', locals())



