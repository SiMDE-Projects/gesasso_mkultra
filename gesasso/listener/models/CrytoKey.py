from django.db import models

from gesasso.api.utils import TimeStampable


class CryptoKey(TimeStampable):
    def __str__(self):
        return self.name

    class KeyType(models.TextChoices):
        RSA = "RSA", "RSA"

    class Agent(models.TextChoices):
        MK_MAIL = "MK_MAIL", "MK_MAIL"

    name = models.CharField(max_length=150)
    type = models.CharField(choices=KeyType.choices, default=KeyType.RSA, max_length=30)
    agent = models.CharField(
        choices=Agent.choices, default=Agent.MK_MAIL, max_length=10
    )
    public_key = models.TextField()
