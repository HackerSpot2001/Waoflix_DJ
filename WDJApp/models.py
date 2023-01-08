from django.db import models as db

class WDJContact(db.Model):
    contact_id = db.BigAutoField
    fname = db.CharField(max_length=25,null=False)
    lname = db.CharField(max_length=25,null=False)
    conMail = db.CharField(max_length=50,null=False)
    phoneNumber = db.CharField(max_length=13,null=False)
    conReason = db.TextField()
    date_created = db.DateTimeField(auto_now_add=True)
    
    def __repr__(self):
        return f"{self.fname} {self.lname} - {self.conMail}"

class WDJComments(db.Model):
    comm_id = db.BigAutoField
    fname = db.CharField(max_length=25,null=False)
    comMail = db.CharField(max_length= 100,null=False)
    comReason = db.TextField()
    date_created = db.DateTimeField(auto_now_add=True)
    
    def __repr__(self):
        return f"{self.fname} - {self.comMail}"

class WDJLogin(db.Model):
    sno = db.AutoField(primary_key=True)
    userName = db.CharField(max_length=25,null=False)
    sess_uuid = db.TextField()
    passWord = db.CharField(max_length=100,null=False)
    date_created = db.DateTimeField(auto_now_add=True)
    
    def __repr__(self):
        return f"{self.sno}"

class WDJUsers(db.Model):
    user_id = db.BigAutoField
    user_uuid_md5 =db.TextField()
    userName = db.CharField(max_length=50,null=False)
    passWord = db.CharField(max_length=100,null=False)
    userEmail = db.CharField(max_length=75,null=False)
    date_created = db.DateTimeField(auto_now_add=True)
    
    def __repr__(self):
        return f"{self.user_id}"

class WDJMovies(db.Model):
    movie_id = db.BigAutoField(primary_key=True)
    slug = db.CharField(max_length=300,null=False)
    poster_url = db.CharField(max_length=300,null=False)
    movie_title = db.CharField(max_length=300,null=False)
    movieRating = db.CharField(max_length=5,null=False)
    movieQuality = db.CharField(max_length=10,null=False)
    movieFileSize = db.CharField(max_length=10,null=False)
    movieLanguage = db.CharField(max_length=20,null=False)
    movieReleaseDate = db.CharField(max_length=20,null=False)
    movieStory = db.TextField()
    movieDownloadURL = db.TextField()
    date_created = db.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"{self.movie_id} - {self.slug}"

