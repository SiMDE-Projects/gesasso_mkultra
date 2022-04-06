from rest_framework import serializers

from gesasso.listener.models import CryptoKey, MailRequest


class MailRequestSerializer(serializers.ModelSerializer):
    """
    ::) :)
    """

    class Meta:
        model = MailRequest
        fields = ["mail_from", "mail_to", "mail_subject", "mail_body"]


class RequestCreatorSerializer(serializers.Serializer):
    """
    Agent's JWT serializer
    """

    agent = serializers.ChoiceField(choices=CryptoKey.Agent.choices)
    token = serializers.CharField(max_length=512)
