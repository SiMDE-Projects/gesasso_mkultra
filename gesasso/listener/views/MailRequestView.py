from rest_framework import viewsets, permissions

from gesasso.listener.models import MailRequest
from gesasso.listener.serializers import MailRequestSerializer


class MailRequestView(viewsets.ModelViewSet):
    """
    :-)
    """

    serializer_class = MailRequestSerializer
    queryset = MailRequest.objects.all()
    permission_classes = [permissions.IsAuthenticated]
