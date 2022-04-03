import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    GESASSO_DJANGO_DEBUG=(bool, False),
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
DEBUG = env.bool("GESASSO_DJANGO_DEBUG")
WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "./frontend/",
        "STATS_FILE": os.path.join(BASE_DIR, "./gesasso/frontend/webpack-stats.json"),
        "CACHE": not DEBUG,
    }
}
