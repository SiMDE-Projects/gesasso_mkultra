from django.db import models
from gesasso.api.utils import TimeStampable
from gesasso.api.models.ActionType import ActionType


class Action(TimeStampable):
    name = models.CharField(unique=True, max_length=150)
    type = models.ForeignKey(ActionType, on_delete=models.CASCADE)
