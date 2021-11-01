from django.db import models

from gesasso.api.models.ActionType import ActionType
from gesasso.api.utils import TimeStampable


class Action(TimeStampable):
    def __str__(self):
        return self.name

    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, blank=False, null=False, max_length=150)
    type = models.ForeignKey(ActionType, on_delete=models.CASCADE)
