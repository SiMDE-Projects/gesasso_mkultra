from django.db import models

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

    class Origin(models.IntegerChoices):
        MAIL = 1, "MAIL"
        DIRECT = 2, "DIRECT"
        MERGE = 3, "MERGE"

    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=False, null=False, max_length=150)
    description = models.TextField()
    due_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey("User", on_delete=models.DO_NOTHING)
    asso = models.ForeignKey("Asso", on_delete=models.DO_NOTHING)
    status = models.PositiveSmallIntegerField(
        choices=Status.choices, default=Status.OPEN
    )
    origin = models.PositiveSmallIntegerField(
        choices=Origin.choices, default=Origin.DIRECT
    )
