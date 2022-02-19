from rest_framework import serializers

from gesasso.api.models import RequestMessage
from gesasso.api.serializers.UserSerializer import UserSerializer


class RequestMessageSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    type = serializers.SerializerMethodField()
    origin = serializers.SerializerMethodField()

    def get_type(self, obj):
        return obj.get_type_display()

    def get_origin(self, obj):
        return obj.get_origin_display()

    class Meta:
        model = RequestMessage
        fields = [
            "url",
            "id",
            "request",
            "user",
            "message",
            "type",
            "origin",
            "created",
        ]
