from django.urls import path
from . import views

app_name = "admin"

urlpatterns = [
    #ADMIN SIGNUP
    path('signup', views.signup, name='signup'),

    #ADMIN SIGNIN
    path('signin', views.signin, name='signin'),

    #ADMIN SIGNUP
    path('signout', views.signout, name='signout'),
    
    #DASHBOARD
    path('admin/dashboard', views.dashboard, name="admin-dashboard"),
    path('admin/dashboard/<str:id>', views.user_detail, name="user-detail"),

]