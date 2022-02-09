from uuid import UUID

from django.db.transaction import atomic
from oauth_pda_app.utils import get_api

from gesasso.proxy_pda.models import Asso


def sync_assos(request):
    r = get_api(request, "/assos")
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
