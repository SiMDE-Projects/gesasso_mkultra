from django.db import models
from gesasso.api.utils import TimeStampable


class ActionType(TimeStampable):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, blank=False, null=False, max_length=150)
    tasks = models.ManyToManyField("Task", blank=True)
    tasks_types = models.ManyToManyField("TaskType")
