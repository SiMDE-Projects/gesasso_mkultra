import os
from pathlib import Path

import getconf

config = getconf.ConfigGetter("gesasso", ["./local_settings.ini"])
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = config.getbool("django.debug", False)
WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "./frontend/",
        "STATS_FILE": os.path.join(BASE_DIR, "./gesasso/frontend/webpack-stats.json"),
        "CACHE": not DEBUG,
    }
}
