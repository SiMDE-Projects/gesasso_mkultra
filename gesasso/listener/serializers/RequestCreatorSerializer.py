from rest_framework import serializers

from gesasso.listener.models import CryptoKey


class RequestCreatorSerializer(serializers.Serializer):
    """
    Agent's JWT serializer
    """

    agent = serializers.ChoiceField(choices=CryptoKey.Agent.choices)
    token = serializers.CharField(max_length=512)
