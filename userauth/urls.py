from django.urls import path
from . import views

app_name = "userauth"

urlpatterns = [

    # HOME
    path('home', views.home, name="home"),

    # DASHBOARD
    path('user/dashboard/<str:id>/', views.dashboard, name="user-dashboard")
]
