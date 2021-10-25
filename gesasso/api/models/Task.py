from django.db import models
from gesasso.api.utils import TimeStampable
from gesasso.api.models.TaskType import TaskType


class Task(TimeStampable):
    name = models.CharField(unique=True, max_length=150)
    type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
