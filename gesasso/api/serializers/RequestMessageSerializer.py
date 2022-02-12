from rest_framework import serializers

from gesasso.api.models import RequestMessage


class RequestMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequestMessage
        fields = ["url", "request", "user", "message", "is_readable"]
