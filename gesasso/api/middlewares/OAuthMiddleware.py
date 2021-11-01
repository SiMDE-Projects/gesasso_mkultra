import logging

from authlib.integrations.base_client import OAuthError
from authlib.integrations.django_client import OAuth
from authlib.oauth2.rfc6749 import OAuth2Token
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from gesasso import settings
from gesasso.api import views

logger = logging.getLogger(__name__)


class OAuthMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)
        self.oauth = OAuth()

    def process_request(self, request):
        if settings.OAUTH_URL_WHITELISTS is not None:
            for w in settings.OAUTH_URL_WHITELISTS:
                if request.path.startswith(w):
                    return self.get_response(request)

        def update_token(token, refresh_token, access_token):
            request.session["token"] = token
            return None

        sso_client = self.oauth.register(
            settings.OAUTH_CLIENT_NAME,
            overwrite=True,
            **settings.OAUTH_CLIENT,
            update_token=update_token
        )
        if request.path.startswith("/oauth/callback"):
            self.clear_session(request)
            request.session["token"] = sso_client.authorize_access_token(request)
            current_user = self.get_current_user(sso_client, request)
            if current_user is not None:
                request.META["REMOTE_USER"] = current_user
                redirect_uri = request.session.pop("redirect_uri", None)
                if redirect_uri is not None:
                    return redirect(redirect_uri)
                return redirect(views.index)

        if request.session.get("token", None) is not None:
            current_user = self.get_current_user(sso_client, request)
            if current_user is not None:
                request.META["REMOTE_USER"] = current_user
                return self.get_response(request)
        # remember redirect URI for redirecting to the original URL.
        request.session["redirect_uri"] = request.path
        return sso_client.authorize_redirect(
            request, settings.OAUTH_CLIENT["redirect_uri"]
        )

    # fetch current login user info
    # 1. check if it's in cache
    # 2. fetch from remote API when it's not in cache
    @staticmethod
    def get_current_user(sso_client, request):
        token = request.session.get("token", None)
        if token is None or "access_token" not in token:
            return None

        if not OAuth2Token.from_dict(token).is_expired() and "user" in request.session:
            return request.session["user"]

        try:
            res = sso_client.get(
                settings.OAUTH_CLIENT["userinfo_endpoint"], token=OAuth2Token(token)
            )
            assos = sso_client.get(
                "/api/v1/user/assos", token=OAuth2Token(token)
            ).json()
            if res.ok:
                request.session["user"] = res.json()
                request.session["user"]["assos"] = assos
                return request.session["user"]
        except OAuthError as e:
            logger.error(e)
        return None

    @staticmethod
    def clear_session(request):
        try:
            del request.session["user"]
            del request.session["token"]
        except KeyError:
            pass

    def __del__(self):
        logger.error("destroyed")
