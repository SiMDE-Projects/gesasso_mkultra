from rest_framework import generics, viewsets, permissions

from gesasso.listener.models import MailRequest
from gesasso.listener.serializers import MailRequestSerializer


class CreateTriageRequest(generics.CreateAPIView):
    """
    Vue qui renvoie la liste des associations dont l'utilisateur
    connecté fait partie. Le retour tient compte de la
    hiérarchie des associations.
    """

    serializer_class = MailRequestSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        """
        Construit la queryset adaptée à l'utilisateur
        """

        return MailRequest.objects.all()


class TriageRequestView(viewsets.ModelViewSet):
    """
    :-)
    """

    serializer_class = MailRequestSerializer
    queryset = MailRequest.objects.all()
    permission_classes = [permissions.IsAuthenticated]
