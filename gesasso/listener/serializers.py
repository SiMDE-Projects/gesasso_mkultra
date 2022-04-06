from rest_framework import serializers

from gesasso.listener.models import MailRequest


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
        fields = ["mail_from", "mail_to", "mail_subject", "mail_body"]
