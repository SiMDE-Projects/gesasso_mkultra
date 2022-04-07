from rest_framework import serializers

from gesasso.listener.models import MailRequest


class MailRequestSerializer(serializers.ModelSerializer):
    """
    ::) :)
    """

    class Meta:
        model = MailRequest
        fields = ["mail_from", "mail_to", "mail_subject", "mail_body"]
