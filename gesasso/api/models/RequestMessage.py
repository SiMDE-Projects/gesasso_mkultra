from django.db import models
from oauth_pda_app.models import User

from gesasso.api.models import Request
from gesasso.api.utils import TimeStampable


class RequestMessage(TimeStampable):
    class Types(models.TextChoices):
        PUBLIC = "PUBLIC", "PUBLIC"
        INTERNAL = "INTERNAL", "INTERNAL"
        SUCCESS = "SUCCESS", "SUCCESS"
        ERROR = "ERROR", "ERROR"
        INFO = "INFO", "INFO"

    class Origin(models.TextChoices):
        WEB = "WEB", "WEB"
        MAIL = "MAIL", "MAIL"
        DIRECT = "DIRECT", "DIRECT"

    id = models.AutoField(primary_key=True)
    request = models.ForeignKey(
        Request, on_delete=models.CASCADE, related_name="messages"
    )
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    custom_author_name = models.CharField(max_length=254, blank=True, null=True)
    type = models.CharField(choices=Types.choices, default=Types.PUBLIC, max_length=25)
    origin = models.CharField(
        choices=Origin.choices, default=Origin.DIRECT, max_length=25
    )
