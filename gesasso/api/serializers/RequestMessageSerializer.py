from rest_framework import serializers

from gesasso.api.models import RequestMessage
from gesasso.api.serializers.AttachementSerializer import AttachementSerializer
from gesasso.api.serializers.UserSerializer import UserSerializer


class RequestMessageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    type = serializers.ChoiceField(choices=RequestMessage.Types)
    origin = serializers.ChoiceField(choices=RequestMessage.Origin)
    attachements = AttachementSerializer(many=True, read_only=True)

    def get_type(self, obj):
        return obj.get_type_display()

    def get_origin(self, obj):
        return obj.get_origin_display()

    class Meta:
        model = RequestMessage
        fields = [
            "id",
            "request",
            "user",
            "custom_author_name",
            "message",
            "type",
            "origin",
            "created",
            "attachements",
        ]
