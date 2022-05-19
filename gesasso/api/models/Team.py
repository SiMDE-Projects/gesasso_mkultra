from django.db import models
from oauth_pda_app.models import User

from gesasso.api.utils import TimeStampable


class Team(TimeStampable):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=False, max_length=50)
    members = models.ManyToManyField(User, related_name="teams")
