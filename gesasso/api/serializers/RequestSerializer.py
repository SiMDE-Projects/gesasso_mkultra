from rest_framework import serializers

from gesasso.api.models import Request


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ["url", "title", "asso", "user", "status", "due_date", "origin", "actions", "messages"]
