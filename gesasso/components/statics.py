import os
from pathlib import Path

import environ

env = environ.Env(
    BASE_URL=(str, "/"),
)
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = env("BASE_URL") + "static/"
STATIC_ROOT = "/static"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "gesasso", "frontend", "dist"),)
