from django.urls import path
from . import views


# Waoflix URLConf
urlpatterns = [
    path('',view=views.temp_mail,name='TempMail Home'),
    path('getmailcontent',view=views.getIncomingMails,name='TempMail Content'),
    path('messages/<slug>',view=views.getMailMessage,name='TempMail Content'),
]