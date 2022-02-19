from rest_framework import serializers

from gesasso.api.models import ActionType


class ActionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionType
        fields = ["url", "id", "name"]
