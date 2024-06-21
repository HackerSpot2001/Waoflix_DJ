from django.shortcuts import render,HttpResponse
from Modules.utils import data,generateRandomAvataar,createAvatar
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps

# Create your views here.
@csrf_exempt # Ignoreing CSRF Token
def avatar(req):
    data["title"] = "Avatar Creator"
    if (req.method == "POST"):
        mydata = []
        jsondata = list(dict(loads(req.body)).values())
        for i in jsondata:
            mydata.append(i)
        
        png = createAvatar(mydata=mydata)
        return HttpResponse(dumps({"status":"OK","msg":"Avatar Created Successfully","png":png}))

    if (req.method == "GET"):
        pngFile = generateRandomAvataar()
        data['png'] = pngFile

    return render(req,"avatar.html",context=data)
