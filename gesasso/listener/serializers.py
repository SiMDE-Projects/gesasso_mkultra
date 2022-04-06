from rest_framework import serializers

from listener.models import MailRequest


class UserInfoSerializer(serializers.Serializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    email = serializers.CharField()
    id = serializers.UUIDField()


class MailRequestSerializer(serializers.ModelSerializer):
    """
    ::) :)
    """

    class Meta:
        model = MailRequest
        fields = ["from", "to", "subject", "content"]
