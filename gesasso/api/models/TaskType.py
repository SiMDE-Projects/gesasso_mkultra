from django.db import models
from gesasso.api.utils import TimeStampable


class TaskType(TimeStampable):
    name = models.CharField(unique=True, max_length=150)
