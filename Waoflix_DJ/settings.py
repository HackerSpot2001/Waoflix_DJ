import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '5467nuhc=+elubk@hwq(cf!*m@kp0d*w=ot*_j04ihv*!is*g+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['192.168.1.70','127.0.0.1','192.168.133.66']
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'WDJApp.apps.WdjappConfig',
    'WDJAvatar.apps.WdjavatarConfig',
    'WDJUsers.apps.WdjusersConfig',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'Waoflix_DJ.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Waoflix_DJ.wsgi.application'


# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'waoflix',
        'USER': 'web',
        'PASSWORD': 'password',
        'HOST':'localhost',
        'PORT':'3306',
    }
}




# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR , "static"),
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ORIGIN_ALLOW_ALL = True
ADMIN_ENABLED = False

# DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
# DBBACKUP_STORAGE_OPTIONS = {'location': 'djwaoflix/db__backup'}


# ADMIN_ENABLED = True
# CORS_ORIGIN_ALLOW_ALL = False
# CORS_ORIGIN_WHITELIST = (
#   'http://localhost:8000',
# )



"""
CSP_REPORT_URI = '<add your reporting uri>'
  
# default source as self
CSP_DEFAULT_SRC = ("'self'", )
  
# style from our domain and bootstrapcdn
CSP_STYLE_SRC = ("'self'", 
    "stackpath.bootstrapcdn.com")
  
# scripts from our domain and other domains
CSP_SCRIPT_SRC = ("'self'",
    "ajax.cloudflare.com",
    "static.cloudflareinsights.com",
    "www.google-analytics.com",
    "ssl.google-analytics.com",
    "cdn.ampproject.org",
    "www.googletagservices.com",
    "pagead2.googlesyndication.com"
)
  
# images from our domain and other domains
CSP_IMG_SRC = ("'self'",
    "www.google-analytics.com",
    "raw.githubusercontent.com",
    "googleads.g.doubleclick.net"
)
  
# loading manifest, workers, frames, etc
CSP_FONT_SRC = ("'self'", )
CSP_CONNECT_SRC = ("'self'", 
    "www.google-analytics.com" )
CSP_OBJECT_SRC = ("'self'", )
CSP_BASE_URI = ("'self'", )
CSP_FRAME_ANCESTORS = ("'self'", )
CSP_FORM_ACTION = ("'self'", )
CSP_INCLUDE_NONCE_IN = ('script-src', )
CSP_MANIFEST_SRC = ("'self'", )
CSP_WORKER_SRC = ("'self'", )
CSP_MEDIA_SRC = ("'self'", )
"""