import logging

from django.http import JsonResponse
from oauth_pda_app.models import User
from rest_framework import viewsets, permissions

from gesasso.api.serializers import UserSerializer

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class SelfUserViewSet(viewsets.GenericViewSet):
    """
    API endpoint that allows users get own datas.
    """

    queryset = User.objects.all()

    def get(self, request):
        # return JsonResponse(request.session["user"])
        # response = call_get_api(request, '/user')
        response = {}
        return JsonResponse(response)
