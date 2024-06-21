from django.urls import path
from . import views


# Waoflix URLConf
urlpatterns = [
    path('',view=views.home,name='Waoflix Home'),
    path('login/',view=views.login,name='Waoflix Login'),
    path('admin-dashboard/',view=views.admin_dashboard,name='Waoflix Admin Dashboard'),
    path('logout/',view=views.logout,name='Waoflix Logout'),
    path('comment/',view=views.comments,name='Waoflix Comment'),
    path('upload_movie/',view=views.upload_movie,name='Waoflix Uploader'),
    path('update_movie/',view=views.update_movie,name='Waoflix Update'),
    path('watch/',view=views.watch,name='Waoflix Watch'),
    # path('watch/<slug>',view=views.watch_movie,name='Waoflix Watch Movie'),
    path('watch/<slug:slug>',view=views.watch_movie,name='Waoflix Watch Movie'),
]
