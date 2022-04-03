import os

import dj_database_url
import environ
import getconf

env = environ.Env(
    GESASSO_DB_DEFAULT=(str, ""),
    GESASSO_DJANGO_SECRET=(str, "whatever"),
)
# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
config = getconf.ConfigGetter("gesasso", ["./local_settings.ini"])
if env("GESASSO_DJANGO_SECRET") != "whatever":
    database = None
    if env("GESASSO_DJANGO_SECRET") != "":
        database = dj_database_url.parse(env("GESASSO_DB_DEFAULT"))
    DATABASES = {
        "default": database
        if database
        else dj_database_url.parse(env("GESASSO_DB_DEFAULT"))
    }
    DATABASES["default"]["ENGINE"] = "django.db.backends.mysql"
