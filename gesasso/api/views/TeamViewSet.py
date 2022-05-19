import logging

from rest_framework import viewsets, permissions

from gesasso.api.models import Team
from gesasso.api.serializers import TeamSerializer
from gesasso.api.utils import TrackerMixin

logger = logging.getLogger(__name__)


class TeamViewSet(TrackerMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAdminUser]
