import logging

from rest_framework import viewsets, permissions

from gesasso.api.models import Request
from gesasso.api.serializers import (
    RequestSerializer,
)

logger = logging.getLogger(__name__)


class RequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows requests to be viewed or edited.
    """

    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]
