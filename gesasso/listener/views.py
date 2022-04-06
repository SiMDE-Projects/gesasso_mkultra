import re

import jwt
from django.db.transaction import atomic
from django.views.decorators.csrf import csrf_exempt
from oauth_pda_app.models import User
from rest_framework import viewsets, permissions
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response

from gesasso.api.middlewares import CsrfExemptSessionAuthentication
from gesasso.api.models import Request, RequestMessage
from gesasso.listener.models import MailRequest, CryptoKey
from gesasso.listener.serializers import MailRequestSerializer


class RequestCreatorView(viewsets.ViewSet):
    """
    Vue qui recoit les JWT des agents et qui créé les metarequests associées
    """

    permission_classes = [permissions.AllowAny]
    authentication_classes = [CsrfExemptSessionAuthentication]
    """
    Test data:
    good mail req 2
    {"agent":"MK_MAIL","token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWJqZWN0IjoiW0dBUl8yXXNxZHFzZHFzZCIsImZyb20iOiJDZXNhciBSaWNoYXJkIDxjZXNhci5yaWNoYXJkQHV0Yy5mcj4iLCJ0byI6InNpbWRlQGFzc29zLnV0Yy5mciIsImJvZHkiOiJcblxuLS0gXG5DZXNhciBSaWNoYXJkXG5cblxuXG5cbi0tIFxuXG5cbj1cbkNlc2FyIFJpY2hhcmRcblxuXG5cblxuXG4ifQ.I953Uo2knvsn7dziS87sGNNEz8prVCQZUMGl_ktoftGNzc4LqgITtVYaewT07TYSydVe4STbK7hGEI7m0EwJl27zPRT9nSBMls57ILa2kXgArlA8B45nDjWtFJU_GepeaQCICMR6tcBL_Eqzgv4EuTYcZBzm2hDaRuYcS7GIlX8"}
    mail sujet foireux
    {"agent":"MK_MAIL","token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWJqZWN0IjoiW0dBUl8gMl1zcWRxc2Rxc2QiLCJmcm9tIjoiQ2VzYXIgUmljaGFyZCA8Y2VzYXIucmljaGFyZEB1dGMuZnI-IiwidG8iOiJzaW1kZUBhc3Nvcy51dGMuZnIiLCJib2R5IjoiXG5cbi0tIFxuQ2VzYXIgUmljaGFyZFxuXG5cblxuXG4tLSBcblxuXG49XG5DZXNhciBSaWNoYXJkXG5cblxuXG5cblxuIn0.azqBAH5CFwQKW73JZaVceLpOioZZdCYP78coVg_JKrbHeQ3Ew52V0kZKXVCPgnDmKoh-OHg4n1O1ND1H04p-BcFv9L9fgQm0v7F8z4_Nd74_v9gdOA9LO-cU-1XxwLWHzIGJodYLbead4hS7HdlENx8cM4NZw_LAHNizz1EwHf4"}
    """

    @csrf_exempt
    def create(self, request):
        print(request.data["agent"])
        key = CryptoKey.objects.get(agent=request.data["agent"], removed=None)
        decoded = jwt.decode(
            request.data["token"], key.public_key, algorithms=["RS256"]
        )
        subject = decoded["subject"]

        from_ = re.search(r"[\w.+-_]+@[\w-]+\.[\w.-]+", decoded["from"]).group(0)
        # to = re.search(r"([\w.+-_]+)@[\w-]+\.[\w.-]+", decoded["to"])
        body = decoded["body"]
        user = None

        try:
            user = User.objects.get(email=from_)
        except User.DoesNotExist:
            pass
        custom_user = None if user is None else decoded["from"]
        request_id_match = re.search(r"\[GAR_(\d)+\]", subject)
        with atomic():
            if request_id_match:
                req = Request.objects.get(pk=request_id_match.group(1))
            else:
                req = Request.objects.create(
                    title=subject,
                    origin=Request.Origin.MAIL,
                    custom_author_name=custom_user,
                    user=user,
                )
                req.save()
            RequestMessage.objects.create(
                request=req,
                message=body,
                origin=RequestMessage.Origin.MAIL,
                custom_author_name=custom_user,
                user=user,
            )

        return Response("OK")

    def list(self, request):
        raise MethodNotAllowed("GET")

    def retrieve(self, request, pk=None):
        raise MethodNotAllowed("GET")

    def update(self, request, pk=None):
        raise MethodNotAllowed("PUT")

    def partial_update(self, request, pk=None):
        raise MethodNotAllowed("PATCH")

    def destroy(self, request, pk=None):
        raise MethodNotAllowed("DELETE")


class MailRequestView(viewsets.ModelViewSet):
    """
    :-)
    """

    serializer_class = MailRequestSerializer
    queryset = MailRequest.objects.all()
    permission_classes = [permissions.IsAuthenticated]
