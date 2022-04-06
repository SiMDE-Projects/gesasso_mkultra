import re

import jwt
from django.db.transaction import atomic
from django.views.decorators.csrf import csrf_exempt
from oauth_pda_app.models import User
from rest_framework import viewsets, permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from gesasso.api.middlewares import CsrfExemptSessionAuthentication
from gesasso.api.models import Request, RequestMessage
from gesasso.listener.models import CryptoKey, MailRequest


class RequestCreatorView(viewsets.ViewSet):
    """
    Vue qui recoit les JWT des agents et qui créé les metarequests associées
    """

    permission_classes = [permissions.AllowAny]
    authentication_classes = [CsrfExemptSessionAuthentication]

    @csrf_exempt
    def create(self, request):
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
        custom_user = decoded["from"] if user is None else None
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
            if request.data["agent"] == CryptoKey.Agent.MK_MAIL:
                MailRequest.objects.create(
                    request=req,
                    mail_from=from_,
                    mail_to=decoded["to"],
                    mail_subject=subject,
                    mail_body=body,
                )
            else:
                raise ValidationError("Unknown Gesasso agent")
        return Response("OK", status=status.HTTP_201_CREATED)
