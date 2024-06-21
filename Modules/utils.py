
from .python_avatars import Avatar
from cairosvg import svg2png
from uuid import uuid4
from hashlib import md5
from django.db.models import Q
from .mail import Email



data = {
    "title":"Home",
    "logUrl":"/waoflix/login",
    "logContent":"Login",
}


fileName = "static/avatar.svg"
pngFile = "static/avatar.png"

def generateRandomAvataar(filename=None):
    if (filename == None):
        filename = fileName
    avatar = Avatar()
    avatar.happy()
    avatar.render(filename)
    return changeToPng(filename)

def changeToPng(filename=None):
    uuid = generate_uuid()
    pngFile2 = f"{pngFile}-{uuid}.png"
    print(pngFile2)
    with open(filename,"r") as f:
        svg_code = f.read()
    svg2png(bytestring=svg_code,write_to=pngFile2)
    return pngFile2

def createAvatar(mydata,filename=None):
    if (filename == None):
        filename = fileName
        # print(filename)
    try:
        avatar = Avatar(
                style=mydata[0],
                background_color=mydata[1],
                top=mydata[2],
                eyebrows=mydata[3],
                eyes=mydata[4],
                nose=mydata[5],
                mouth=mydata[6],
                facial_hair=mydata[7],
                skin_color=mydata[8],
                hair_color=mydata[9],
                accessory=mydata[10],
                clothing=mydata[11],
                clothing_color=mydata[12]
            )
        avatar.render(filename)
        return changeToPng(filename)
    except Exception as e:
        print("Error,",e)

def generate_uuid():
    return str(uuid4())

def generate_md5(uuid:str):
    return md5(uuid.encode("utf-8")).hexdigest()



def startMailServer(listener):
    mailServer = Email()
    mailServer.register()
    mail_data  = {
        'domain': mailServer.domain,
        'email_id': mailServer.address,
        'password': mailServer.password
    }
    mailServer.start(listener)
    return mail_data
    
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

