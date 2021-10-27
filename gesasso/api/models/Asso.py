from django.db import models


class Asso(models.Model):
    id = models.UUIDField(primary_key=True)
    login = models.CharField(max_length=30)
    shortname = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
