from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Trader, TraderData
import random
from datetime import datetime, timedelta

# Create your views here.

# HOME VIEW
def home(request):
    traders = Trader.objects.all()

    context={
        "traders":traders
    }
    return render(request, "interfaces/home.html", context)



# USER DASHBOARD VIEW
def dashboard(request, id):

    rand = random.randint(1,100)
    

    trader_id = Trader.objects.get(id=id)
    trader = TraderData.objects.order_by("-profit_loss")[:1]

    context = {
        "trader_id":trader_id,
        "trader":trader,
        "rand":rand
    }
    return render(request, "interfaces/user_dashboard.html", context)
