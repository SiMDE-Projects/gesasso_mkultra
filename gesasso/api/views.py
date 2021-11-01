import logging

import requests
from django.contrib.auth.models import Group
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from gesasso import settings
from gesasso.api.models import Asso, Action, Request, User
from gesasso.api.serializers import (
    UserSerializer,
    GroupSerializer,
    AssoSerializer,
    RequestSerializer,
    ActionSerializer,
)

logger = logging.getLogger(__name__)


class AssosViewSet(viewsets.ModelViewSet):
    queryset = Asso.objects.all()
    serializer_class = AssoSerializer
    can_create = False
    can_change = False
    can_delete = False

    def list(self, request, *args, **kwargs):
        r = requests.get("%s/assos" % settings.OAUTH_CLIENT["api_base_url"])
        datas = r.json()
        bulk_delete = []
        for data in datas:
            if data["in_cemetery_at"] or data["in_cemetery_at"]:
                bulk_delete.append(data["id"])
            else:
                Asso.objects.update_or_create(
                    id=data["id"],
                    defaults={
                        "login": data["login"],
                        "shortname": data["shortname"],
                        "name": data["name"],
                        "parent": Asso(data["parent"]["id"])
                        if data["parent"]
                        else None,
                    },
                )
        (Asso.objects.filter(pk__in=bulk_delete)).delete()
        return Response(datas)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ActionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows actions to be viewed or edited.
    """

    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    permission_classes = [permissions.IsAuthenticated]


class RequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows requests to be viewed or edited.
    """

    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]
