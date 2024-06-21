from django.urls import path
from . import views


urlpatterns = [
    path('',view=views.user_home,name='Users Home'),
    path('login',view=views.user_login,name='Users Login'),
    path('logout',view=views.user_logout,name='Users Logout'),
    path('forget-password',view=views.users_forget,name='Forget Password'),
    path('dashboard',view=views.users_dashboard,name='Users Dashboard'),
    path('register',view=views.user_register,name='Users Register'),
]