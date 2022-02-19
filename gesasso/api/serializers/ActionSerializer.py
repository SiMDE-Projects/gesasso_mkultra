from rest_framework import serializers

from gesasso.api.models import Action, ActionType


class ActionSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=ActionType.objects.all(),
    )

    class Meta:
        model = Action
        fields = ["url", "id", "name", "type"]
