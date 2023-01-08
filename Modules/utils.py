# from .python_avatars import AvatarStyle,AccessoryType,Avatar,BackgroundColor,ClothingColor,ClothingType,EyebrowType,EyeType,FacialHairType,HairColor,HairType,MouthType, SkinColor,NoseType
from .python_avatars import Avatar
from cairosvg import svg2png
from uuid import uuid4
from hashlib import md5
from WDJApp.models import WDJLogin as  waoflixLogin, WDJUsers as waoflixUsers
from django.db.models import Q
from bcrypt import gensalt,checkpw,hashpw

data = {
    "title":"Home",
    "logUrl":"/waoflix/login",
    "logContent":"Login",
}

session_uuid = list(waoflixLogin.objects.filter(Q(sno__icontains='1')))[0]

# avatarData = [
#     AvatarStyle,
#     BackgroundColor,
#     HairType, # Top
#     EyebrowType,
#     EyeType,
#     NoseType,
#     MouthType,
#     FacialHairType,
#     SkinColor,
#     HairColor,
#     AccessoryType,
#     ClothingType,
#     ClothingColor,
# ]
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

def checkSession(req):
    try:
        session = req.session.get('sid')
        # print(session_uuid.sess_uuid)
        user_session = generate_md5(session_uuid.sess_uuid)
        if (session != None):
            if session == user_session:
                data['logUrl'] = '/waoflix/logout'
                data['logContent'] = 'Logout'
                return True

            else:
                data['logUrl'] = '/waoflix/login'
                data['logContent'] = 'Login'
                return False

        else:
            data['logUrl'] = '/waoflix/login'
            data['logContent'] = 'Login'
            return False
    except Exception as e:
        print("Error: ",str(e))
        return False

def checkCookie(req):
    try:
        cookie = req.COOKIES.get('cookieId')
        # cookie = "fbeb3298abb250fc7a3750d2ff542fdd"
        if (cookie != None):
            user = waoflixUsers.objects.get(user_uuid_md5=cookie)
            return True

    except Exception as e:
        print("Error: ",str(e))
        return False

def createHash(password):
    hashValue = hashpw(str(password).encode("utf-8"),gensalt(12))
    return hashValue.decode("utf-8")

def verify_hash(hash_value,password):
    if checkpw(password.encode("utf-8"),hashed_password=hash_value.encode("utf-8")):
        return True

    else:
        return False