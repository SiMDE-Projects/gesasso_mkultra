import os

import environ

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env(
    GESASSO_BASE_URL=(str, "/"),
    GESASSO_STATIC_URL=(str, "static/"),
    GESASSO_STATIC_ROOT=(str, os.path.join(BASE_DIR, "static")),
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
STATIC_URL = env("GESASSO_BASE_URL") + env("GESASSO_STATIC_URL", "static/")
STATIC_ROOT = env("GESASSO_STATIC_ROOT")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "gesasso", "frontend", "dist"),)
