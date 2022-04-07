from rest_framework import serializers

from gesasso.api.models import Request
from gesasso.proxy_pda.serializers import AssoSerializer
from . import ActionSerializer, RequestMessageSerializer
from .UserSerializer import UserSerializer


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    asso = AssoSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    actions = ActionSerializer(many=True, read_only=True)
    messages = RequestMessageSerializer(many=True, read_only=True)
    status = serializers.ChoiceField(choices=Request.Status)
    origin = serializers.ChoiceField(choices=Request.Origin)

    def get_assignees(self, obj):
        """self referral field"""
        serializer = UserSerializer(obj.assignees.all(), many=True)
        return serializer.data

    class Meta:
        model = Request
        fields = [
            "id",
            "url",
            "title",
            "asso",
            "user",
            "custom_author_name",
            "status",
            "due_date",
            "origin",
            "actions",
            "messages",
            "assignees",
            "created",
        ]
