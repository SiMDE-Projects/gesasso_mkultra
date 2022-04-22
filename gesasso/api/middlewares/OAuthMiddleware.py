import logging

from django.contrib.auth import login
from django.utils.deprecation import MiddlewareMixin
from oauth_pda_app.backend import OAuthBackend

from gesasso.proxy_pda.serializers import UserInfoSerializer
from gesasso.proxy_pda.utils import request_user_assos

logger = logging.getLogger(__name__)


class OAuthMiddleware(MiddlewareMixin):
    """
    Middleware to handle OAuth2 authentication.
    """

    def __init__(self, get_response=None):
        super().__init__(get_response)

    def process_request(self, request):
        """
        Process the request to check if the user is authenticated.
        """
        sessions_keys = request.session.keys()
        if "token" in sessions_keys and not request.user.is_authenticated:
            datas = UserInfoSerializer(request.session["user"])
            user = OAuthBackend().authenticate(request, datas.data)
            login(request, user)
            if "assos" not in request.session.keys():
                request.session["assos"] = request_user_assos(request)
            if not (user.is_staff and user.is_superuser):
                for asso in request.session["assos"]:
                    if (
                        asso["login"]
                        == "simde"
                        # and asso["pivot"]["role_id"] == "5e12fc00-3af5-11e9-a2eb-bda2ff28d348"
                    ):
                        logger.info("User is a simde's member")
                        user.is_staff = True
                        user.is_superuser = True
                        user.save()
                        break
