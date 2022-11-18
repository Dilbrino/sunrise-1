from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import request
from django.shortcuts import render, redirect


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
            return redirect('/')
        else:
            messages.info(request, "Invalid password or username")
            return redirect('login-view')

    else:
        return render(request, 'customer_page/login.html')


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
            user = User.objects.create_user(username=username, email=email)
            user.first_name = firstname
            user.last_name = lastname
            user.set_password(password)
            user.save()
            messages.info(request, "Registration successful, choose a car.")
            return redirect('login-view')
        except:
            messages.info(request, "username already exists")
            return render(request, 'customer_page/register.html')

    else:
        return render(request, 'customer_page/register.html')
