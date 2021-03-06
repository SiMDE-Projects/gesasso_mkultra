import requests
from rest_framework.exceptions import NotAuthenticated

from gesasso.proxy_pda.serializers import UserInfoSerializer


def retrieve_user_info(request):
    """
    Fonction qui récupère les informations de l'utilisateur connecté
    """
    if "token" not in request.session.keys():
        # si il n'y a pas de token, on supprime les éventuelles
        # informations utilisateur mises en cache
        if "user" in request.session.keys():
            request.session.pop("user")

        raise NotAuthenticated()
    else:
        if "user" not in request.session.keys():
            # si l'utilisateur n'est pas en cache dans la session, on le
            # récupère depuis le PDA
            token = request.session["token"]
            response = requests.get(
                "https://assos.utc.fr/api/v1/user",
                headers={"Authorization": "Bearer {}".format(token["access_token"])},
            )
            user = UserInfoSerializer(response.json())
            request.session["user"] = user.data

        user = UserInfoSerializer(request.session["user"])

    return user
