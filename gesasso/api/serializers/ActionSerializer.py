from rest_framework import serializers

from gesasso.api.models import Action, ActionType


class ActionSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.HyperlinkedRelatedField(
        view_name="actiontype-detail",
        lookup_field="id",
        required=False,
        queryset=ActionType.objects.all(),
    )

    class Meta:
        model = Action
        fields = ["url", "id", "name", "type"]
