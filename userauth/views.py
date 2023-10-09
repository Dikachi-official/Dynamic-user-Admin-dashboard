from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Trader
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
    trader = Trader.objects.get(id=id)
    current_time = datetime.now()

    #GENERATE A RANDOM PROFIT OR LOSS
    profit_loss = random.uniform(-10, 100)

    #UPDATE TRADER BALANCE
    trader.balance +=profit_loss
    trader.save()

    #ONE MIN TIME INTERVAL CALC
    one_min_ago = current_time - timedelta(minutes=1)

    #GETTING PROFIT AND LOSS FOR A RANDOM TRADER
    profit_loss_data = {}
    data_points = trader.traderdata_set.filter(timestamp__gte=one_min_ago, timestamp__lte=current_time)
    profit_loss_data[trader.name] = [(data.timestamp, data.profit_loss) for data in data_points]


    context = {
        "trader":trader,
        "profit_loss_data": profit_loss_data
    }
    return render(request, "interfaces/user_dashboard.html", context)
