from rest_framework import serializers

from gesasso.api.models import Attachement


class AttachementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachement
        fields = [
            "id",
            "name",
            "type",
            "data",
            "created",
        ]
