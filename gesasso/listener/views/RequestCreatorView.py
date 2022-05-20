import base64
import logging
import re

import jwt
from django.core.files.base import ContentFile
from django.db.transaction import atomic
from django.views.decorators.csrf import csrf_exempt
from oauth_pda_app.models import User
from rest_framework import viewsets, permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from gesasso.api.middlewares import CsrfExemptSessionAuthentication
from gesasso.api.models import Request, RequestMessage
from gesasso.listener.models import CryptoKey, MailRequest
from gesasso.proxy_pda.models import Asso

logger = logging.getLogger(__name__)


class RequestCreatorView(viewsets.ViewSet):
    """
    Vue qui recoit les JWT des agents et qui créé les metarequests associées
    """

    permission_classes = [permissions.AllowAny]
    authentication_classes = [CsrfExemptSessionAuthentication]

    @csrf_exempt
    def create(self, request):
        iss = jwt.decode(request.data["token"], options={"verify_signature": False})[
            "iss"
        ]
        key = CryptoKey.objects.get(agent=iss, removed=None)
        decoded = jwt.decode(
            jwt=request.data["token"],
            key=key.public_key,
            algorithms=["RS256"],
            audience="MK_ULTRA",
        )
        subject = decoded["subject"]

        from_ = re.search(r"<?([\w+-_]+@[\w-]+\.[\w.-]+)>?", decoded["from"]).group(1)
        to = re.search(r"<?([\w+-_]+@[\w-]+\.[\w.-]+)>?", decoded["to"]).group(1)
        body = decoded["body"]
        user = None
        asso = None

        try:
            user = User.objects.get(email=from_)
        except User.DoesNotExist:
            pass
        try:
            asso = Asso.objects.get(login=from_.split("@")[0])
        except Asso.DoesNotExist:
            pass
        custom_user = decoded["from"] if user is None else None
        request_id_match = re.search(r"\[GAR_(\d+)]", subject)

        with atomic():
            if request_id_match:
                req = Request.objects.get(pk=request_id_match.group(1))
            else:
                req = Request.objects.create(
                    title=subject,
                    origin=Request.Origin.MAIL,
                    custom_author_name=custom_user,
                    user=user,
                    asso=asso,
                )
                req.save()
            rm = RequestMessage.objects.create(
                request=req,
                message=body,
                origin=RequestMessage.Origin.MAIL,
                custom_author_name=custom_user,
                user=user,
            )
            if iss == CryptoKey.Agent.MK_MAIL:
                MailRequest.objects.create(
                    request=req,
                    mail_from=from_,
                    mail_to=to,
                    mail_subject=subject,
                    mail_body=body,
                )
                if decoded["attachements"]:
                    for att in decoded["attachements"]:
                        att_data = ContentFile(
                            base64.b64decode(att["content"]), att["name"]
                        )
                        att_name = att["name"]
                        att_type = att["type"]
                        rm.attachements.create(
                            name=att_name,
                            type=att_type,
                            data=att_data,
                        )
            else:
                raise ValidationError("Unknown Gesasso agent")

        return Response({"id": req.id}, status=status.HTTP_201_CREATED)
