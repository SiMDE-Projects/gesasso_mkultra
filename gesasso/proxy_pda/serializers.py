from rest_framework import serializers

from gesasso.proxy_pda.models import Asso


class UserInfoSerializer(serializers.Serializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    email = serializers.CharField()
    id = serializers.UUIDField()


class AssoSerializer(serializers.ModelSerializer):
    """
    Serializer permettant de renvoyer la liste des associations dont
    un utilisateur fait partie
    """

    class Meta:
        model = Asso
        fields = [
            "id",
            "shortname",
            "name",
        ]
