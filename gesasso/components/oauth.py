import getconf

config = getconf.ConfigGetter("gesasso", ["./local_settings.ini"])

OAUTH_SETTINGS = {
    "client_id": config.getstr("OAUTH_SETTINGS_ID"),
    "client_secret": config.getstr("OAUTH_SETTINGS_SECRET"),
    "authorization_url": "https://assos.utc.fr/oauth/authorize",
    "token_url": "https://assos.utc.fr/oauth/token",
    "redirect_uri": "http://localhost:8003/oauth/callback",
    "scopes": ["user-get-info", "user-get-roles", "user-get-assos"],
    "api_base_url": "https://assos.utc.fr/api/v1",
}
