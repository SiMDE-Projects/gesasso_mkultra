from django.db import models

from gesasso.api.utils import Model


class Asso(Model):
    def __str__(self):
        return "{} ({})".format(self.shortname, self.login)

    id = models.UUIDField(primary_key=True)
    login = models.CharField(max_length=30)
    shortname = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)
