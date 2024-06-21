from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view=views.home,name='Home'),
    path('contact/',view=views.contact,name='Contact'),
    path('about/',view=views.about,name='About'),
    path('waoflix/',include('WDJApp.urls')),
    path('users/',include('WDJUsers.urls')),
    path('avatar/',include('WDJAvatar.urls')),
    path('tempmail/',include("WDJTempMail.urls")),
]
