import logging

from django.core.mail import send_mail
from django.db.models import Q
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

    queryset = RequestMessage.objects.all().order_by("-created")
    serializer_class = RequestMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Override the default get_queryset method to filter by user.
        """
        request = self.request.query_params.get("request", None)
        if request:
            self.queryset = self.queryset.filter(request__id=request)

        if self.request.user.is_superuser:
            return self.queryset

        return self.queryset.filter(
            (Q(user=self.request.user) & Q(type=RequestMessage.Types.INTERNAL))
            | ~Q(type=RequestMessage.Types.INTERNAL)
        )

    def perform_create(self, serializer):
        """
        Override the default perform_create method to add the user
        to the request.
        """
        with atomic():
            serializer.save(user=self.request.user)
            send_mail(
                serializer.instance.request.title,
                serializer.instance.message,
                "gesasso@assos.utc.fr",
                ["cesar@assos.utc.fr"],
            )
        super(RequestMessageViewSet, self).perform_create(serializer)
