

from pathlib import Path
from datetime import time, timedelta
from os import getenv
from django.db.models.manager import BaseManager
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR/".env")

IS_PRODUCTION = False
if getenv("IS_PRODUCTION") in ['True', 'true']:
    IS_PRODUCTION = True


USE_AWS_S3 = False
if getenv("USE_AWS_S3") in ['True', 'true']:
    USE_AWS_S3 = True

USE_SQLITE = False
if getenv("USE_SQLITE") in ['True', 'true']:
    USE_SQLITE = True
    SQLITE_FILENAME = getenv("SQLITE_FILENAME", "db.sqlite3")


USE_MYSQL = False
if getenv("USE_MYSQL") in ['True', 'true']:
    USE_MYSQL = True
    DB_NAME = getenv("DB_NAME")
    DB_PORT = getenv("DB_PORT")
    DB_HOST = getenv("DB_HOST")
    DB_USER = getenv("DB_USER")
    DB_PASSWORD = getenv("DB_PASSWORD")


APP_HOST = getenv('APP_HOST', 'localhost')
PAGE_SIZE = int(getenv("PAGE_SIZE", 10))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=j6!^gj$w)oxbzi2i#!$sh7y4zqzfo1804o7j60(5vkyoks4n!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not IS_PRODUCTION


ALLOWED_HOSTS = [APP_HOST]
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1)
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'storages',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_simplejwt',
    'rest_framework',

    'django_filters',
    'core',
    'course',
    'chapter',
    'coupon',
    'doubt',
    'order',
    'review',
]


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': PAGE_SIZE
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'feelfreetocode.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'feelfreetocode.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

database_setup = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': str(BASE_DIR / 'db.sqlite3'),
}

if USE_SQLITE:
    database_setup = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / SQLITE_FILENAME),
    }


if USE_MYSQL:
    database_setup = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'PORT': DB_PORT,
        'HOST': DB_HOST,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD
    }


DATABASES = {
    'default': database_setup
}
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/files/'
MEDIA_ROOT = BASE_DIR/"files"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# AWS KEYS

if USE_AWS_S3:
    AWS_ACCESS_KEY_ID = getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = getenv("AWS_SECRET_ACCESS_KEY")
    AWS_S3_REGION_NAME = getenv("AWS_S3_REGION_NAME")
    AWS_STORAGE_BUCKET_NAME = getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    STATICFILES_STORAGE = 'feelfreetocode.custom_storage.StaticFilesStorage'
    DEFAULT_FILE_STORAGE = 'feelfreetocode.custom_storage.MediaFilesStorage'

    MEDIA_FILES_LOCATION = 'uploaded-files'
    STATIC_FILES_LOCATION = 'static-files'
