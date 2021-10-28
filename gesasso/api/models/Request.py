from django.db import models

from django.utils.translation import ugettext_lazy as _
from gesasso.api.utils import TimeStampable


class Request(TimeStampable):
    def __str__(self):
        return self.title

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
    description = models.TextField()
    user = models.CharField(blank=False, null=False, max_length=150)
    asso = models.ForeignKey("Asso", on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(
        choices=Status.choices, default=Status.OPEN
    )
    actions = models.ManyToManyField("Action")
