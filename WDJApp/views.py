from django.shortcuts import render,redirect
from WDJApp.models import WDJLogin as waoflixLogin, WDJMovies as waoflixMovies, WDJComments as WaoFlixComments
from Modules.utils import data
from django.contrib import auth as  authentication 
from django.contrib.auth.decorators import login_required

# from django.db.models import Q
# from Modules.utils import data,generate_md5,checkSession


# Waoflix Views
# loginCreds = waoflixLogin(userName="tH3uNKn0WnW40Fl1x",passWord="\+<%vQDWM4Fc'9^S",sess_uuid="b3bc4bf3-19c9-449d-a00c-410dd8195004")
# loginCreds.save()


# session_uuid = list(waoflixLogin.objects.filter(Q(sno__icontains='1')))[0]
# total_movies = waoflixMovies.objects.count()

def home(req):
    try:
        data["title"] = "Home"
        pages = 10 # total_movies
        limit = 20
        page = int(req.GET.get('page',1))
        page = int(req.GET.get('page',1))

        if page < 1 : page = 1
        
        offset = (page - 1) * limit
        data["prev"] = str( int(page - 1))
        data["next"] = str(int(page+1))
        pages = int((pages/limit)+1)
        data["showmsg"] = "Latest Movies and Web-Series"
        movies = waoflixMovies.objects.order_by('-movie_id').all()[ offset : offset+limit :-1]
        data["pagesText"] = f"{page} of {pages}"
        data['movies'] = list(reversed(movies))

    except:
        data["prev"] = "1"
        data["next"] = "1"
        data['movies'] = []
        data["pagesText"] = ""
        data["showmsg"] = "There is some error"
    
    return render(req,'index.html',context=data)

    # checkSession(req)



def login(req):
    data['title'] = "Login in Waoflix"
    if req.method == "GET":
        if ( req.user.is_authenticated ):
            return redirect('/waoflix/admin-dashboard')


    if req.method == "POST":
        username = req.POST.get('username',None)
        password = req.POST.get('password',None)
        print(username)
        print(password)
        if (username != None and password != None):
            user = authentication.authenticate(req, username=username,password=password)
            if (user is None): print("User not found.") 
            authentication.login(req, user)
            return redirect('/waoflix/admin-dashboard')

        else:
            data['showMsg'] = "Invalid authentication"

    
    return render(req,'login.html',context=data)
    



@login_required(login_url='/waoflix/login',)
def upload_movie(req):
    data['title'] = "Upload an Movie"
    if req.method == "GET":
        return render(req,'uploader.html',context=data)

    if req.method == "POST":
        try:
            if (req.POST["movietitle"] != "") and (req.POST["rating"] != "") and (req.POST["quality"] != "") and (req.POST["fileSize"] != "") and (req.POST["language"] != "") and (req.POST["releasedate"] != "") and (req.POST["desc"] != "") and (req.POST["downloadUrl"] != ""):
                upload = waoflixMovies(
                    slug=str(req.POST["movietitle"]).replace(" ","-").replace(".","_"),
                    poster_url=req.POST["poster"],
                    movie_title=req.POST["movietitle"],
                    movieRating=str(req.POST["rating"]),
                    movieQuality=req.POST["quality"],
                    movieFileSize=req.POST["fileSize"],
                    movieLanguage=req.POST["language"],
                    movieReleaseDate=req.POST["releasedate"],
                    movieStory=req.POST["desc"],
                    movieDownloadURL=req.POST["downloadUrl"],
                    )
                upload.save()   
                data['showMsg'] = "Movie uploaded successfully."

        except Exception as e:
            data['showMsg'] = "Error, something went wrong!"
            print ("Error: ", str(e))
        
        return render(req,'uploader.html',context=data)


@login_required(login_url='/waoflix/login')
def update_movie(req):
    data['title'] = "Update an Movie"
    try:
        if req.method == "POST":
            if (req.POST["movietitle"] != "") and (req.POST["rating"] != "") and (req.POST["quality"] != "") and (req.POST["fileSize"] != "") and (req.POST["language"] != "") and (req.POST["releasedate"] != "") and (req.POST["desc"] != "") and (req.POST["downloadUrl"] != "" ) and (req.POST["sno"] != "" ):
                movie = waoflixMovies.objects.get(movie_id=str(req.POST.get('sno')))
                if (movie != None):
                    movie.movie_title = req.POST.get("movietitle")
                    movie.poster_url = req.POST.get("poster")
                    movie.movieRating = req.POST.get("rating")
                    movie.movieReleaseDate = req.POST.get("quality")
                    movie.movieFileSize = req.POST.get("fileSize")
                    movie.movieReleaseDate = req.POST.get("releasedate")
                    movie.movieDownloadURL = req.POST.get("downloadUrl")
                    movie.movieStory = req.POST.get("desc")
                    movie.movieLanguage = req.POST.get("language")
                    movie.save()
                    data['showMsg'] = "Movie updated successfully."

                else:
                    data['showMsg'] = "Error, something went wrong!"

        if req.method == "GET":
            movie = waoflixMovies.objects.get(movie_id=str(req.GET.get('id')))
            data['movie'] = movie

    except Exception as e:
        print(e)
        data['showMsg'] = "Error, something went wrong!"
   
    return render(req,'update.html',context=data)


@login_required(login_url='/waoflix/login')
def admin_dashboard(req):
    movies = waoflixMovies.objects.all()
    data['movies'] = list(movies)
    return render(req,'dashboard.html',context=data)


def watch_movie(req,slug):
    try:
        movie = waoflixMovies.objects.get(slug=str(slug))
        user_comments = WaoFlixComments.objects.order_by('-id').all()
        data['movie'] = movie
        data['title'] = "Watch {}".format(str(slug))
        data['comments'] = list(user_comments)
    except Exception as e:
        print("ErrorL :",str(e))
        data['movie'] = ""
    
    return render(req,"watch.html",context=data)


def watch(req):
    return redirect('/waoflix')


def logout(req):
    authentication.logout(req)
    return redirect('/')
    

def comments(req):
    if req.method == "POST":
        if ((req.POST['comName'] != "") and (req.POST['comMail'] != "") and (req.POST['commentReason'] != "") ):
            comm = WaoFlixComments(fname=str(req.POST.get("comName")),comMail=str(req.POST.get("comMail")),comReason=str(req.POST.get("commentReason")))
            comm.save()

    return redirect('/')
