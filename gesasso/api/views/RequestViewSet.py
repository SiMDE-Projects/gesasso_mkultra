import logging

from django.db.transaction import atomic
from rest_framework import viewsets, permissions

from gesasso.api.models import Request, RequestMessage
from gesasso.api.serializers import RequestSerializer
from gesasso.api.utils import TrackerMixin
from gesasso.proxy_pda.models import Asso

logger = logging.getLogger(__name__)


class RequestViewSet(TrackerMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows requests to be viewed or edited.
    """

    queryset = (
        Request.objects.all()
        .order_by("-created")
        .prefetch_related("user", "messages", "asso")
    )
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Override the default perform_create method to add the user
        to the request.
        """
        with atomic():
            asso = Asso.objects.get(pk=self.request.data["asso"]["id"])
            request = serializer.save(user=self.request.user, asso=asso)
            RequestMessage.objects.create(
                request=request,
                user=self.request.user,
                message=self.request.data["message"],
            )
        super(RequestViewSet, self).perform_create(serializer)
