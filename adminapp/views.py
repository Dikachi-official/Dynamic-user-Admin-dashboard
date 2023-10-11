from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from userauth.models import Trader, TraderData
import random

# Create your views here.


# ADMIN SIGNUP
def signup(request):
    if request.user.is_authenticated:
        messages.warning(
            request, f"Hey {request.user} you are already logged in.")
        return redirect('adminapp:admin-dashboard')
    if request.method == "POST":
        # username = request.POST.get/
        username = request.POST['name']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # if we query database and see inputed username exist then reply
        if User.objects.filter(username=username):
            messages.error(
                request, "name already exists! Please try another username")
            return redirect('adminapp:signup')

        if pass1 != pass2:
            messages.error(request, "Passwords don't match")
            return redirect('adminapp:signup')

        if not username.isalnum():  # If username is something other than alpha-numeric
            messages.error(request, "name must be Alphanumeric")
            return redirect('adminapp:signup')

        # pass these input to the object adminapp
        myadmin = User.objects.create_user(username, pass1)
        myadmin.username = username  # pass name input to the myuser object
        myadmin.save()
        login(request, myadmin)

        # pop up message after registration
        messages.success(
            request, "Your Account has been successfully created.")
        return redirect("adminapp:admin-dashboard")

    return render(request, "interfaces/signup.html")


# SIGNIN VIEW
def signin(request):
    if request.user.is_authenticated:
        messages.warning(
            request, f"Hey {request.user} you are already logged in.")
        return redirect('adminapp:admin-dashboard')
    if request.method == "POST":
        # COMPARE INPUT WITH DATABASE
        username = request.POST['name']
        password = request.POST['pass1']
        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request, f"User with {username} doesn't exists ☹")    
            return redirect('adminapp:signin')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            username = user.username
            return redirect("adminapp:admin-dashboard")

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
    if request.user.is_authenticated:
        traders = Trader.objects.all()

        context = {
            "traders": traders
        }

        return render(request, "interfaces/admin_dashboard.html", context)
    else:
        messages.warning(request, "Log in to gain access")
        return redirect("adminapp:signup")
    



def user_detail(request, id):
    if request.user.is_authenticated:
        labels = []
        data = []

        rand = random.randint(0,100)

        trader_id = Trader.objects.get(id=id)
        trader = TraderData.objects.order_by("-profit_loss")[:10]
        for t in trader:
            labels.append(t.trader)
            data.append(t.profit_loss)

        context = {
            "trader_id":trader_id,
            "trader":trader,
            "labels":labels,
            "data":data,
            "rand":rand
        }

        return render(request, "interfaces/admin_dash_detail.html", context)
    else:
        messages.warning(request, "Log in to gain access")
        return redirect("adminapp:signup")
