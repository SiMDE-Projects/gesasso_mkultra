import getconf

config = getconf.ConfigGetter("gesasso", ["./local_settings.ini"])
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
