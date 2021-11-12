from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    objects = models.Manager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50, blank=False, null=False)
