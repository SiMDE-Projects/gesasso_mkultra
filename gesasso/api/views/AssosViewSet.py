import logging

from rest_framework import viewsets
from rest_framework.response import Response

from gesasso import settings
from gesasso.proxy_pda.models import Asso
from gesasso.proxy_pda.serializers import AssoSerializer
from gesasso.proxy_pda.utils import sync_assos

logger = logging.getLogger(__name__)


class AssosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Asso.objects.all()
    serializer_class = AssoSerializer

    def list(self, request, force=False, *args, **kwargs):
        if force or not settings.DISABLE_SYNC_ASSOS:
            sync_assos(request)
        return Response(self.queryset.values())
