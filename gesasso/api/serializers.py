from django.contrib.auth.models import User, Group
from rest_framework import serializers

from gesasso.api.models import Request, Action, Asso, ActionType


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


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


class AssoSerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField(required=False, method_name="get_parent")

    def get_parent(self, obj):
        """self referral field"""
        serializer = AssoSerializer(pk=obj.parent.id)
        return serializer.data

    class Meta:
        model = Asso
        fields = ["id", "login", "shortname", "parent"]


class ActionSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.HyperlinkedRelatedField(
        view_name="actiontype-detail",
        lookup_field="id",
        required=False,
        queryset=ActionType.objects.all(),
    )

    class Meta:
        model = Action
        fields = ["url", "id", "name", "type"]


class ActionTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActionType
        fields = ["url", "id", "name", "tasks_types_set"]


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ["url", "user", "actions"]
