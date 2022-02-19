import logging

from django.contrib.auth.models import Group
from rest_framework import viewsets, permissions

from gesasso.api.serializers import GroupSerializer
from gesasso.api.utils import TrackerMixin

logger = logging.getLogger(__name__)


class GroupViewSet(TrackerMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
