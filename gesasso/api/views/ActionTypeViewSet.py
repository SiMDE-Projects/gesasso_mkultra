import logging

from rest_framework import viewsets, permissions

from gesasso.api.models import ActionType
from gesasso.api.serializers import ActionTypeSerializer

logger = logging.getLogger(__name__)


class ActionTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows actions to be viewed or edited.
    """

    queryset = ActionType.objects.all()
    serializer_class = ActionTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
