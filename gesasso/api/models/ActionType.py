from django.db import models
from gesasso.api.utils import TimeStampable
from gesasso.api.models.TaskType import TaskType


class ActionType(TimeStampable):
    name = models.CharField(unique=True, max_length=150)
    tasks = models.ManyToManyField(TaskType)
