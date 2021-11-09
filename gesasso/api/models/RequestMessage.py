from django.db import models

from gesasso.api.models import Request
from gesasso.api.utils import TimeStampable


class RequestMessage(TimeStampable):
    class Types(models.IntegerChoices):
        PUBLIC = 1, "PUBLIC"
        INTERNAL = 2, "INTERNAL"
        SUCCESS = 3, "SUCCESS"
        ERROR = 4, "ERROR"
        INFO = 5, "INFO"

    id = models.AutoField(primary_key=True)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    message = models.TextField()
    user = models.ForeignKey("User", on_delete=models.DO_NOTHING)
    type = models.PositiveSmallIntegerField(choices=Types.choices, default=Types.PUBLIC)
