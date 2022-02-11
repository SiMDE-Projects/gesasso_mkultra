from django.contrib.auth.models import User
from rest_framework import serializers

from api.serializers import GroupSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = [
            "url",
            "username",
            "first_name",
            "last_name",
            "email",
            "groups",
        ]
