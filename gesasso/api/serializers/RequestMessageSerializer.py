from rest_framework import serializers

from gesasso.api.models import RequestMessage
from gesasso.api.serializers.UserSerializer import UserSerializer

class RequestMessageSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = RequestMessage
        fields = ["url", "request", "user", "message"]
