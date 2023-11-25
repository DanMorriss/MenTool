"""
Django settings for mentool project.
"""

import os
from pathlib import Path

# load environment variables file
import dj_database_url
from dotenv import load_dotenv

if os.path.isfile(".env"):
    load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG")

# CLOUDINARY URL from environment variable
CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL")

ALLOWED_HOSTS = ["*",
    "https://8000-danmorriss-mentool-1t3kh0d7w2b.ws-eu106.gitpod.io", "https://8000-agyluczak-mentool-gabrkhljn7k.ws-eu106.gitpod.io",
    "mentool-2af96fd6f7e7.herokuapp.com/", '8000-email2ify-mentool-2ezcnhxci5.us2.codeanyapp.com', "https://thephelpster-mentool-3eh4js6905k.ws-eu106.gitpod.io", "*",]  # TODO: "*" to be removed
    

CSRF_TRUSTED_ORIGINS = [
    "https://8000-email2ify-mentool-2ezcnhxci5.us2.codeanyapp.com",
    "https://8000-agyluczak-mentool-gabrkhljn7k.ws-eu106.gitpod.io",
    "https://thephelpster-mentool-3eh4js6905k.ws-eu106.gitpod.io",]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "cloudinary_storage",
    "django.contrib.staticfiles",
    "cloudinary",
    "crispy_forms",
    "crispy_bootstrap4",
    "tracker",
]

# Crispy Forms Settings
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mentool.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mentool.wsgi.application"


# Database

DATABASES = {
   "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) and Cloudinary Settings

STATIC_URL = "static/"
STATICFILES_STORAGE = \
    "cloudinary_storage.storage.StaticHashedCloudinaryStorage"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = "/media/"
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Add login url
LOGIN_URL = "login"
