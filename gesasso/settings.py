import logging.config
import os
from pathlib import Path

import dj_database_url
import getconf
from django.utils.log import DEFAULT_LOGGING

config = getconf.ConfigGetter("gesasso", ["./local_settings.ini"])

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.getstr("django.secret")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.getbool("django.debug", False)

ALLOWED_HOSTS = config.getlist("django.allowed_hosts", ["*"])

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "storages",
    # "debug_toolbar",
    "gesasso.api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "gesasso.api.middlewares.OAuthMiddleware",
    "django.contrib.auth.middleware.RemoteUserMiddleware",
]

AUTHENTICATION_BACKENDS = [
    "gesasso.api.middlewares.RemoteAuthBackend",
]

AUTH_USER_MODEL = "api.User"

if DEBUG:
    import socket  # only if you haven't already imported this

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

ROOT_URLCONF = "gesasso.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "gesasso.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if config.getstr("DJANGO_SECRET") != "whatever":
    database = None
    if config.getstr("db.secret") != "":
        database = dj_database_url.parse(config.getstr("db.default"))
    DATABASES = {
        "default": database
        if database
        else dj_database_url.parse(config.getstr("db.default"))
    }
    DATABASES["default"]["ENGINE"] = "django.db.backends.mysql"

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = "/static"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

CORS_ORIGIN_ALLOW_ALL = True

# OAuth Settings
OAUTH_URL_WHITELISTS = ["/__debug__"]

OAUTH_CLIENT_NAME = "portailutc"

OAUTH_CLIENT = {
    "client_id": config.getstr("OAUTH_CLIENT_ID"),
    "client_secret": config.getstr("OAUTH_CLIENT_SECRET"),
    "access_token_url": "https://assos.utc.fr/oauth/token",
    "authorize_url": "https://assos.utc.fr/oauth/authorize",
    "api_base_url": "https://assos.utc.fr/api/v1",
    "redirect_uri": "http://localhost:8003/oauth/callback",
    "client_kwargs": {
        "scope": "user-get-info user-get-roles-users-assigned user-get-roles user-get-assos-members-joined-now"
    },
    "userinfo_endpoint": "/api/v1/user",
}

LOGLEVEL = os.environ.get("LOGLEVEL", "DEBUG").upper()

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                # exact format is not important, this is the minimum information
                "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
            },
            "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
        },
        "handlers": {
            # console logs to stderr
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
            "django.server": DEFAULT_LOGGING["handlers"]["django.server"],
        },
        "loggers": {
            # default for all undefined Python modules
            "": {
                "level": "DEBUG",
                "handlers": ["console"],
            },
            # Our application code
            "app": {
                "level": LOGLEVEL,
                "handlers": ["console"],
                # Avoid double logging because of root logger
                "propagate": False,
            },
            # Default runserver request logging
            "django.server": DEFAULT_LOGGING["loggers"]["django.server"],
        },
    }
)
