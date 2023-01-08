from django.urls import path
from . import views


# Waoflix URLConf
urlpatterns = [
    path('',view=views.avatar,name='Avatar Home'),
]