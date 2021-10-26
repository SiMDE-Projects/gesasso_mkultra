from django.db import models
from gesasso.api.utils import TimeStampable
from gesasso.api.models.ActionType import ActionType


class Request(TimeStampable):
    class Status(models.IntegerChoices):
        OPEN = 1, "OPEN"
        ASSIGNED = 2, "ASSIGNED"
        CLOSED = 3, "CLOSED"
        DONE = 4, "DONE"
        WAITING_TECH = 5, "WAITING_TECH"
        WAITING_FOR_TIERS_SERVICE = 6, "WAITING_FOR_TIERS_SERVICE"
        WAITING_FOR_CUSTOMER = 7, "WAITING_FOR_CUSTOMER"

    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=False, null=False, max_length=150)
    type = models.ForeignKey(ActionType, on_delete=models.CASCADE)
    description = models.TextField()
    user = models.CharField(blank=False, null=False, max_length=150)
    asso = models.CharField(max_length=150)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.OPEN)