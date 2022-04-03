import os

import environ

env = environ.Env(
    GESASSO_BASE_URL=(str, "/"),
    GESASSO_STATIC_URL=(str, "/static/"),
    GESASSO_STATIC_ROOT=(str, "/static/"),
)

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
STATIC_URL = env("STATIC_URL")
STATIC_ROOT = env("STATIC_ROOT")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "gesasso", "frontend", "dist"),)
