from django.shortcuts import render,redirect
from django.http import HttpResponse
from Modules.utils import  data,checkCookie,checkSession,generate_md5,generate_uuid,createHash,verify_hash
from WDJApp.models import WDJUsers as waoflixUsers

def users_dashboard(req):
    data['title'] = "Users Dashboard"
    checkSession(req)
    if (not checkCookie(req)):
        return redirect("/users/login")

    return render(req,"users_admin.html",context=data)

    
def user_login(req):
    try:
        data['title'] = "Users Login"
        checkSession(req)
        
        if req.method == "POST":
            username = req.POST.get("ulname")
            password = req.POST.get("ulpass")
            user = waoflixUsers.objects.get(userName=username)
            if(user and verify_hash(user.passWord,password)):
                res = redirect('/users/dashboard')
                res.set_cookie('cookieId',str(user.user_uuid_md5),max_age=3600,httponly=True,secure=True,path='/users/')
                return res

        
            else:
                data['showMsg'] = "Pls Check your Login Credentials!"
            
                
        if (checkCookie(req)):
            return redirect('/users/dashboard')
    

    except Exception as e:
        print("Error while login: ",str(e))
        data['showMsg'] = "Pls Check your Login Credentials!"
    

    return render(req,'loginforusers.html',context=data)

    
def user_logout(req):
    res = redirect("/users/login")
    res.delete_cookie("cookieId",'/users/')
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
                    user = waoflixUsers(userName=urname,userEmail=urmail,passWord=str(createHash(urpass)),user_uuid_md5=str(generate_md5(generate_uuid())))
                    user.save()
                    data['showMsg'] = "Please Login to Proceed"
                    return redirect('/users/login')
                    

                else:
                    data['showMsg'] = "Username is already registered."



            else:
               data['showMsg'] = "Please check all valid fields!"
        
        if (req.method == "GET"):
               data['showMsg'] = ""

                

    except Exception as e:
        data['showMsg'] = "Please check all valid fields!"
    return render(req,'registerforusers.html',context=data)


    
def users_forget(req):
    return HttpResponse("Users Forget")

    
def user_home(req):
    return redirect("/users/dashboard")

