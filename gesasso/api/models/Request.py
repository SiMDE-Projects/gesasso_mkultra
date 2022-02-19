from django.db import models
from oauth_pda_app.models import User

from gesasso.api.utils import TimeStampable
from gesasso.proxy_pda.models import Asso


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
        WEB = 1, "WEB"
        MAIL = 2, "MAIL"
        DIRECT = 3, "DIRECT"
        MERGE = 4, "MERGE"

        def to_representation(self, value):
            return self.choices[value - 1][1]

        def to_internal_value(self, value):
            for choice in self.choices:
                if choice[1] == value:
                    return choice[0]

    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=False, null=False, max_length=150)
    due_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(User, blank=True, related_name="assignees")
    asso = models.ForeignKey(Asso, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(
        choices=Status.choices, default=Status.OPEN
    )
    origin = models.PositiveSmallIntegerField(
        choices=Origin.choices, default=Origin.DIRECT
    )
    actions = models.ManyToManyField("Action", blank=True)
