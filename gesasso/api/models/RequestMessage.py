from django.db import models
from oauth_pda_app.models import User

from gesasso.api.models import Request
from gesasso.api.utils import TimeStampable


class RequestMessage(TimeStampable):
    class Types(models.IntegerChoices):
        PUBLIC = 1, "PUBLIC"
        INTERNAL = 2, "INTERNAL"
        SUCCESS = 3, "SUCCESS"
        ERROR = 4, "ERROR"
        INFO = 5, "INFO"

    class Origin(models.IntegerChoices):
        MAIL = 1, "MAIL"
        DIRECT = 2, "DIRECT"

    id = models.AutoField(primary_key=True)
    request = models.ForeignKey(
        Request, on_delete=models.CASCADE, related_name="messages"
    )
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    type = models.PositiveSmallIntegerField(choices=Types.choices, default=Types.PUBLIC)
    origin = models.PositiveSmallIntegerField(
        choices=Origin.choices, default=Origin.DIRECT
    )

    @property
    def is_readable(self, user=None):
        return self.type == self.Types.PUBLIC or user.is_superuser or self.user == user
