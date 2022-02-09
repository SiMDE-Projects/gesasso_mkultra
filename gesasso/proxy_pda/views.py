from django.contrib.auth.decorators import login_required
from rest_framework import generics, mixins, views
from rest_framework.response import Response

from gesasso.proxy_pda.models import Asso
from gesasso.proxy_pda.serializers import AssoSerializer, UserInfoSerializer
from gesasso.proxy_pda.utils import request_user_assos, retrieve_user_info


class GetUserInfo(views.APIView):
    """
    Vue qui renvoie les informations de l'utilisateur connecté
    """
    serializer_class = UserInfoSerializer

    def get(self, request, *args, **kwargs):
        user = retrieve_user_info(request)
        return Response(user.data)


class GetListAssos(mixins.ListModelMixin, generics.GenericAPIView):
    """
    Vue qui renvoie la liste des associations pour lesquelles l'utilisateur
    connecté a les droits de trésorerie. Le retour tient compte de la
    hiérarchie des associations.
    """
    serializer_class = AssoSerializer

    @login_required
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        """
        Construit la queryset adaptée à l'utilisateur
        """

        # si les associations ne sont pas en cache dans la session, on les
        # récupère et on les met en cache
        if 'assos' not in self.request.session:
            request_user_assos(self.request)

        allowedAssos = self.request.session['assos']

        return Asso.objects.filter(pk__in=allowedAssos)
