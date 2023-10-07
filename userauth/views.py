from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.

# HOME VIEW
def home(request):
    traders = User.objects.all()

    context={
        "traders":traders
    }
    return render(request, "interfaces/home.html", context)



# USER DASHBOARD VIEW
def dashboard(request, id):
    trader = User.objects.get(id=id)

    context = {
        "trader":trader
    }
    return render(request, "interfaces/user_dashboard.html", context)
