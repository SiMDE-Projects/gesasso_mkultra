import logging

from django.db.transaction import atomic
from rest_framework import viewsets, permissions

from gesasso.api.models import RequestMessage
from gesasso.api.serializers import RequestMessageSerializer
from gesasso.api.utils import TrackerMixin

logger = logging.getLogger(__name__)


class RequestMessageViewSet(TrackerMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows requests messages to be viewed or edited.
    """

    queryset = RequestMessage.objects.all()
    serializer_class = RequestMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Override the default perform_create method to add the user
        to the request.
        """
        with atomic():
            serializer.save(user=self.request.user)
        super(RequestMessageViewSet, self).perform_create(serializer)
