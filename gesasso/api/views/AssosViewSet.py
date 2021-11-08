import logging
from uuid import UUID

import requests
from django.db.transaction import atomic
from rest_framework import viewsets
from rest_framework.response import Response

from gesasso import settings
from gesasso.api.models import Asso
from gesasso.api.serializers import (
    AssoSerializer,
)

logger = logging.getLogger(__name__)


class AssosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Asso.objects.all()
    serializer_class = AssoSerializer

    def list(self, request, *args, **kwargs):
        if not settings.DISABLE_SYNC_ASSOS:
            self.sync_assos()
        return Response(self.queryset.values())

    def sync_assos(self):
        r = requests.get("%s/assos" % settings.OAUTH_CLIENT["api_base_url"])
        datas = r.json()
        existing_datas = Asso.objects.all().values()
        bulk_delete = []
        bulk_create = []
        bulk_update = []
        for data in datas:
            existing_asso = next(
                (x for x in existing_datas if x["id"] == UUID(data["id"])), None
            )
            if existing_asso is None:
                asso = Asso(
                    id=data["id"],
                    login=data["login"],
                    shortname=data["shortname"],
                    name=data["name"],
                )
                bulk_create.append(asso)
                if data["parent"]:
                    asso = Asso(
                        id=data["id"],
                        login=data["login"],
                        shortname=data["shortname"],
                        name=data["name"],
                        parent=Asso(data["parent"]["id"]),
                    )
                    bulk_update.append(asso)
            else:
                if data["in_cemetery_at"] or data["in_cemetery_at"]:
                    bulk_delete.append(data["id"])
                else:
                    if (
                        existing_asso["name"] != data["name"]
                        or existing_asso["shortname"] != data["shortname"]
                    ):
                        asso = Asso(
                            id=data["id"],
                            login=data["login"],
                            shortname=data["shortname"],
                            name=data["name"],
                            parent=Asso(data["parent"]["id"])
                            if data["parent"]
                            else None,
                        )
                        bulk_update.append(asso)
        with atomic():
            Asso.objects.bulk_create(bulk_create)
            Asso.objects.bulk_update(
                bulk_update, ["login", "shortname", "name", "parent"]
            )
            (Asso.objects.filter(pk__in=bulk_delete)).delete()
