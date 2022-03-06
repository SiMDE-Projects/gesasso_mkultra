from django.db import models
from oauth_pda_app.models import User

from gesasso.api.utils import TimeStampable
from gesasso.proxy_pda.models import Asso


class Request(TimeStampable):
    def __str__(self):
        return self.title

    class Status(models.TextChoices):
        OPEN = "OPEN", "OPEN"
        ASSIGNED = "ASSIGNED", "ASSIGNED"
        CLOSED = "CLOSED", "CLOSED"
        DONE = "DONE", "DONE"
        WAITING_TECH = "WAITING_TECH", "WAITING_TECH"
        WAITING_FOR_TIERS_SERVICE = (
            "WAITING_FOR_TIERS_SERVICE",
            "WAITING_FOR_TIERS_SERVICE",
        )
        WAITING_FOR_CUSTOMER = "WAITING_FOR_CUSTOMER", "WAITING_FOR_CUSTOMER"

        def to_representation(self, value):
            return self.choices[value - 1][1]

        def to_internal_value(self, value):
            for choice in self.choices:
                if choice[1] == value:
                    return choice[0]

    class Origin(models.TextChoices):
        WEB = "WEB", "WEB"
        MAIL = "MAIL", "MAIL"
        DIRECT = "DIRECT", "DIRECT"
        MERGE = "MERGE", "MERGE"

    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=False, null=False, max_length=150)
    due_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(User, blank=True, related_name="assignees")
    asso = models.ForeignKey(Asso, on_delete=models.CASCADE)
    status = models.CharField(
        choices=Status.choices, default=Status.OPEN, max_length=30
    )
    origin = models.CharField(
        choices=Origin.choices, default=Origin.DIRECT, max_length=30
    )
    actions = models.ManyToManyField("Action", blank=True)
