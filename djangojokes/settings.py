import os
from pathlib import Path
from dotenv import load_dotenv

from django.contrib.messages import constants as messages

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^%ns@$smw%itx!1043hfh^cz6zk^18x0%w(2&=ufs#38^8d%c7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Built-in Django apps
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'crispy_forms',
    'crispy_bootstrap5',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'private_storage',
    'storages',

    # Local apps
    'common.apps.CommonConfig',
    'jobs.apps.JobsConfig',
    'pages.apps.PagesConfig',
    'jokes.apps.JokesConfig',
    'users.apps.UsersConfig',
]

SITE_ID = 1

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

CRISPY_TEMPLATE_PACK = 'bootstrap5'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangojokes.urls'

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

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# private-storage settings
PRIVATE_STORAGE_ROOT = MEDIA_ROOT / 'private/'
PRIVATE_STORAGE_AUTH_FUNCTION = 'private_storage.permissions.allow_staff'

MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

WSGI_APPLICATION = 'djangojokes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jokes',
        'USER': 'postgres',
        'PASSWORD': 'Pandora117!',
        'HOST': 'localhost',
        'PORT': 6623
    }
}

# EMAIL
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
DEFAULT_FROM_EMAIL = 'pandoraparigian@gmail.com'

ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.SignupForm'

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

# AUTHENTICATION SETTINGS
AUTH_USER_MODEL = 'users.CustomUser'

# Login settings (these were missing in your original file)
LOGIN_URL = 'account_login'

# Redirect after login
LOGIN_REDIRECT_URL = 'pages:homepage'

# Redirect after signup
ACCOUNT_SIGNUP_REDIRECT_URL = 'pages:homepage'

# Redirect logged-in users away from login/signup pages
ACCOUNT_AUTHENTICATED_REDIRECT_URL = 'pages:homepage'

## django-allauth settings
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # Default: 'username'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1  # Default: 3
ACCOUNT_EMAIL_REQUIRED = True  # Default: False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Default: 'optional'
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5  # Default: 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300  # Default 300
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'  # Default: '/'
ACCOUNT_USERNAME_REQUIRED = False  # Default: True

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, even w/o `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth`-specific auth methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'django-jokes2025'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_DEFAULT_ACL = None

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_S3_REGION_NAME = 'us-east-2'  

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",  # Change this line
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
}

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_LOCATION = 'static'

STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
DEFAULT_FILE_STORAGE = 'djangojokes.storage_backends.PublicMediaStorage'
PRIVATE_FILE_STORAGE = 'djangojokes.storage_backends.PrivateMediaStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' 

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY") 

# BOTTOM OF settings.py
if os.environ.get('ENVIRONMENT') != 'production':
    from .local_settings import *
# DON'T PUT ANYTHING BELOW THIS
