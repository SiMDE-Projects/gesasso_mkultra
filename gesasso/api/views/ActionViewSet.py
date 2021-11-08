import logging

from rest_framework import viewsets, permissions

from gesasso.api.models import Action
from gesasso.api.serializers import (
    ActionSerializer,
)

logger = logging.getLogger(__name__)


class ActionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows actions to be viewed or edited.
    """

    queryset = Action.objects.all()
    serializer_class = ActionSerializer
    permission_classes = [permissions.IsAuthenticated]
