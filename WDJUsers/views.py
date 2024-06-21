from django.shortcuts import render,redirect
from django.http import HttpResponse
from Modules.utils import  data
from WDJApp.models import WDJUsers as waoflixUsers
from django.contrib.auth.decorators import login_required
from django.contrib import auth as  authentication 


@login_required(login_url='/waoflix/login')
def users_dashboard(req):
    data['title'] = "Users Dashboard"
    if (req.user.is_anonymous):
        return redirect("/users/login")

    return render(req,"users_admin.html",context=data)


# @login_required(login_url='/waoflix/login',)
def user_login(req):
    try:
        data['title'] = "Users Login"
        
        if req.user.is_authenticated :
            return redirect('/users/dashboard')


        if req.method == "POST":
            username = req.POST.get("ulname")
            password = req.POST.get("ulpass")
            user = authentication.aauthenticate(req,username=username,password=password)
            
            if(user is not None):
                authentication.login(req,user)
                return redirect('/users/dashboard')

        
            else:
                data['showMsg'] = "Pls Check your Login Credentials!"
    

    except Exception as e:
        print("Error while login: ",str(e))
        data['showMsg'] = "Pls Check your Login Credentials!"
    

    return render(req,'loginforusers.html',context=data)



def user_logout(req):
    authentication.logout(req)
    res = redirect("/users/login")
    return res
    




def user_register(req):
    try:
        if (req.method == "POST"):
            urname = req.POST.get('urname')
            urmail = req.POST.get('urmail')
            urpass = req.POST.get('urpass')
            urconpass = req.POST.get('urconpass')
            
            if ((urname != "" and urmail != "" and urpass != "" and urconpass != "") and (urpass == urconpass)):
                
                if(len(waoflixUsers.objects.filter(userName=urname).all()) == 0):
                    # user = waoflixUsers(userName=urname,userEmail=urmail,passWord=str(createHash(urpass)),user_uuid_md5=str(generate_md5(generate_uuid())))
                    # user.save()
                    data['showMsg'] = "Please Login to Proceed"
                    return redirect('/users/login')
                    

                else:
                    data['showMsg'] = "Username is already registered."



            else:
               data['showMsg'] = "Please check all valid fields!"
        
        if (req.method == "GET"):
               data['showMsg'] = ""

                

    except Exception as e:
        print (e)
        data['showMsg'] = "Please check all valid fields!"

    return render(req,'registerforusers.html',context=data)


    
def users_forget(req):
    return HttpResponse("Users Forget")


def user_home(req):
    return redirect("/users/dashboard")

