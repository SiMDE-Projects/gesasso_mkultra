from django.db import models
from gesasso.api.utils import TimeStampable


class Task(TimeStampable):
    id = models.AutoField(primary_key=True)
    params = models.JSONField()
    type = models.ForeignKey("TaskType", on_delete=models.CASCADE)
