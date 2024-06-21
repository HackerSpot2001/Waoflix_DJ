from django.shortcuts import render,redirect
from django.http import HttpResponse
from Modules.utils import  data

def home(req):
    return redirect('/waoflix/')

def contact(req):
    data["title"] = "Contact Us"
    return render(req,"contact.html",context=data)

def about(req):
    data["title"] = "About Us"
    return HttpResponse("Under Construction")
