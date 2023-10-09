from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AdminUser
from django.contrib.auth import authenticate, login, logout
from userauth.models import Trader

# Create your views here.


# ADMIN SIGNUP
def signup(request):
    if request.method == "POST":
        # username = request.POST.get/
        name = request.POST['name']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # if we query database and see inputed username exist then reply
        if AdminUser.objects.filter(name=name):
            messages.error(
                request, "name already exists! Please try another username")
            return redirect('adminapp:signup')

        if pass1 != pass2:
            messages.error(request, "Passwords don't match")
            return redirect('adminapp:signup')

        if not name.isalnum():  # If username is something other than alpha-numeric
            messages.error(request, "name must be Alphanumeric")
            return redirect('adminapp:signup')

        # pass these input to the object adminapp
        myadmin = AdminUser.objects.create(name=name, password=pass1)
        myadmin.name = name  # pass name input to the myuser object
        myadmin.save()

        # pop up message after registration
        messages.success(
            request, "Your Account has been successfully created.")
        return redirect('adminapp:signin')

    return render(request, "interfaces/signup.html")


# SIGNIN VIEW
def signin(request):
    if request.method == "POST":

        # COMPARE INPUT WITH DATABASE
        name = request.POST['name']
        pass1 = request.POST['pass1']
        user = authenticate(name=name, password=pass1)

        if user is not None:
            login(request, user)
            name = user.name
            messages.success(request, "welcome {{request.user}}")
            return render(request, "admin_dashboard.html", {'name': name})

        # Not registered send the error mesage below
        else:
            messages.error(request, "Wrong details")
            return redirect('adminapp:signin')
    return render(request, "interfaces/signin.html")


# SIGNOUT VIEW
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('adminapp:signup')




# ADMIN DASHBOARD VIEW
def dashboard(request):
    if request.user.groups.filter(name="admin").exists():

        traders = Trader.objects.all()

        context = {
            "traders": traders
        }

        return render(request, "interfaces/admin_dashboard.html", context)

    else:
        messages.warning(request, 'Accessible to only admins')
        return redirect('userauth:home')


def user_detail(request, id):
    if request.user.groups.filter(name="admin").exists():

        trader = Trader.objects.get(id=id)

        context = {
            "trader":trader
        }

        return render(request, "interfaces/admin_dash_detail.html", context)

    else:
        messages.warning(request, 'Accessible to only admins')
        return redirect('userauth:home')
