import logging

from rest_framework import viewsets, permissions

from gesasso.api.models import ActionType
from gesasso.api.serializers import ActionTypeSerializer
from gesasso.api.utils import TrackerMixin

logger = logging.getLogger(__name__)


class ActionTypeViewSet(TrackerMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows actions to be viewed or edited.
    """

    queryset = ActionType.objects.all()
    serializer_class = ActionTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
