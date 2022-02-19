from oauth_pda_app.utils import get_api
from rest_framework.exceptions import NotAuthenticated


def request_user_assos(request):
    """
    Récupère la liste des associations auxquelles l'utilisateur est
    inscrit depuis le portail des assos

    request: requête django
    """
    if "user" not in request.session.keys():
        raise NotAuthenticated()

    response = get_api(request, "/users/{}/assos".format(request.session["user"]["id"]))

    # On ignore les associations qui ne sont pas auxquelles l'inscription n'est pas validée
    request.session["assos"] = list(
        filter(lambda x: x["pivot"]["validated_by_id"] is not None, response.json())
    )

    return request.session["assos"]
