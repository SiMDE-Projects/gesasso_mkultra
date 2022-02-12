import logging

from rest_framework import viewsets, permissions

from gesasso.api.models import RequestMessage
from gesasso.api.serializers import RequestMessageSerializer

logger = logging.getLogger(__name__)


class RequestMessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows requests messages to be viewed or edited.
    """

    queryset = RequestMessage.objects.all()
    serializer_class = RequestMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
