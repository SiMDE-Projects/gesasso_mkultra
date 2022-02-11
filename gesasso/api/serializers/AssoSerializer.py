from rest_framework import serializers

from gesasso.proxy_pda.models import Asso


class AssoSerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField(required=False, method_name="get_parent")

    def get_parent(self, obj):
        """self referral field"""
        serializer = AssoSerializer(pk=obj.parent.id)
        return serializer.data

    class Meta:
        model = Asso
        fields = ["id", "login", "shortname", "parent"]
