from rest_framework import serializers

from gesasso.api.models import Request
from gesasso.api.serializers import AssoSerializer, RequestMessageSerializer, ActionSerializer
from .UserSerializer import UserSerializer


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    asso = AssoSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    actions = ActionSerializer(many=True)
    messages = RequestMessageSerializer(many=True)
    status = serializers.SerializerMethodField()
    origin = serializers.SerializerMethodField()

    def get_assignees(self, obj):
        """self referral field"""
        serializer = UserSerializer(obj.assignees.all(), many=True)
        return serializer.data

    def get_status(self, obj):
        return obj.get_status_display()

    def get_origin(self, obj):
        return obj.get_origin_display()

    class Meta:
        model = Request
        fields = [
            "id",
            "url",
            "title",
            "asso",
            "user",
            "status",
            "due_date",
            "origin",
            "actions",
            "messages",
            "assignees",
        ]
        read_only_fields = ["messages"]
