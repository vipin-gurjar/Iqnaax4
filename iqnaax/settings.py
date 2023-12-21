from pathlib import Path
import dj_database_url
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-#lpyxfbgvu(yzw7md1dn8slhht06@m=^j)$m#*%_f&4n^vse!v'

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    'home.apps.HomeConfig',
    'about.apps.AboutConfig',
    'blog.apps.BlogConfig',
    'gallery.apps.GalleryConfig',
    'shop.apps.ShopConfig',
    'contact.apps.ContactConfig',
    'account.apps.AccountConfig',
]



MIDDLEWARE = [
   
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'iqnaax.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'iqnaax.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# postgres://iqnaax_db_user:GGSt50HFs6NkhGmvrWcchrVZIYfRylos@dpg-cm1u40fqd2ns73d66710-a.oregon-postgres.render.com/iqnaax_db
DATABASES["default"]=dj_database_url.parse("postgres://iqnaax_db_user:GGSt50HFs6NkhGmvrWcchrVZIYfRylos@dpg-cm1u40fqd2ns73d66710-a/iqnaax_db")



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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_URL = '/static/'

STATICFILES_DIRS=[
    (BASE_DIR/ 'static')
]

STATIC_ROOT=(BASE_DIR/ 'static')

MEDIA_URL='/media/'
MEDIA_ROOT=(BASE_DIR/ 'media')

# STATIC_ROOT = "/var/www/example.com/static/"
# MEDIA_ROOT = '/opt/render/project/src/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/profile/'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SESSION_ENGINE = "django.contrib.sessions.backends.db"

TINYMCE_DEFAULT_CONFIG = {
    'height': 500,
    'width': 572,
    'menubar': True,
    'plugins': 'advlist autolink link image lists charmap print preview',
    'toolbar': 'styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
    'content_css': [
        '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
        '/static/css/custom_tinymce.css',  
    ],
    'image_advtab': True,
}

JAZZMIN_SETTINGS = {
    "welcome_sign" : "Welcome to IQNAAX Admin",
}





