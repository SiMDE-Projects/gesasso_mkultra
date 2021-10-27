from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from gesasso.api.models import Asso
from gesasso.api.serializers import (
    UserSerializer,
    GroupSerializer,
    AssoSerializer,
)
from gesasso import settings
from rest_framework.response import Response
import requests


class AssosViewSet(viewsets.ModelViewSet):
    queryset = Asso.objects.all()
    serializer_class = AssoSerializer

    def list(self, request, *args, **kwargs):
        r = requests.get("%s/assos" % settings.OAUTH_CLIENT["api_base_url"])
        datas = r.json()
        for data in datas:
            if data["in_cemetery_at"] or data["in_cemetery_at"]:
                print(data)
                try:
                    Asso.objects.delete(id=data["id"])
                finally:
                    continue
            Asso.objects.update_or_create(
                id=data["id"],
                defaults={
                    "login": data["login"],
                    "shortname": data["shortname"],
                    "name": data["name"],
                },
            )

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
