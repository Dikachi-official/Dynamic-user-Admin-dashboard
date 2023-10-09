from django.urls import path
from . import views

app_name = "adminapp"

urlpatterns = [
    #ADMIN SIGNUP
    path('signup', views.signup, name='signup'),

    #ADMIN SIGNIN
    path('signin', views.signin, name='signin'),

    #ADMIN SIGNUP
    path('signout', views.signout, name='signout'),
    
    #DASHBOARD
    path('dashboard', views.dashboard, name="admin-dashboard"),
    path('dashboard/<str:id>', views.user_detail, name="user-detail"),

]