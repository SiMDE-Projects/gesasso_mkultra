from oauth_pda_app.models import User
from rest_framework import serializers

from gesasso.api.serializers import GroupSerializer


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "groups",
            "teams",
        ]
