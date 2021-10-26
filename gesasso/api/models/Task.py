from django.db import models
from gesasso.api.utils import TimeStampable
from gesasso.api.models.TaskType import TaskType


class Task(TimeStampable):
    id = models.AutoField(primary_key=True)
    params = models.JSONField()
    type = models.ForeignKey("TaskType", on_delete=models.CASCADE)
