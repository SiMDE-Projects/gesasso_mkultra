import os
from pathlib import Path

import environ

env = environ.Env(
    GESASSO_OAUTH_SETTINGS_ID=(str, ""),
    GESASSO_OAUTH_SETTINGS_SECRET=(str, ""),
    GESASSO_OAUTH_REDIRECT_URI=(str, "http://localhost:8003/oauth/callback"),
)

BASE_DIR = Path(__file__).resolve().parent.parent
# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

OAUTH_SETTINGS = {
    "client_id": env("GESASSO_OAUTH_SETTINGS_ID"),
    "client_secret": env("GESASSO_OAUTH_SETTINGS_SECRET"),
    "authorization_url": "https://assos.utc.fr/oauth/authorize",
    "token_url": "https://assos.utc.fr/oauth/token",
    "redirect_uri": env("GESASSO_OAUTH_REDIRECT_URI"),
    "scopes": ["user-get-info", "user-get-roles", "user-get-assos"],
    "api_base_url": "https://assos.utc.fr/api/v1",
}
