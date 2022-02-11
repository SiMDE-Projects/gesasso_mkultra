from rest_framework import serializers

from gesasso.api.models import ActionType


class ActionTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActionType
        fields = ["url", "id", "name"]
