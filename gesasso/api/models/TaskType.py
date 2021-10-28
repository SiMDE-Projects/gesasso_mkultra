from django.db import models
from gesasso.api.utils import TimeStampable


class TaskType(TimeStampable):
    def __str__(self):
        return self.name

    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, blank=False, null=False, max_length=150)
    target = models.CharField(blank=False, null=False, max_length=150)
