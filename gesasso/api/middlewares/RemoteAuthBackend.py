import logging

from django.contrib.auth.backends import RemoteUserBackend

logger = logging.getLogger(__name__)


class RemoteAuthBackend(RemoteUserBackend):
    def authenticate(self, request, remote_user):
        user = super(RemoteAuthBackend, self).authenticate(request, remote_user["id"])
        user.first_name = remote_user["firstname"]
        user.last_name = remote_user["lastname"]
        user.email = remote_user["email"]
        for asso in remote_user["assos"]:
            if (
                asso["login"]
                == "simde"
                # and asso["pivot"]["role_id"] == "5e12fc00-3af5-11e9-a2eb-bda2ff28d348"
            ):
                logger.info("User is a simde's member")
                user.is_staff = True
                user.is_superuser = True
        user.save()
        return user
