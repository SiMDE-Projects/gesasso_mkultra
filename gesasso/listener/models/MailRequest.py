from django.db import models

from gesasso.api.models import Request
from gesasso.api.utils import TimeStampable


class MailRequest(TimeStampable):
    def __str__(self):
        return "{} <{}>".format(self.mail_subject, self.mail_from)

    mail_from = models.EmailField()
    mail_to = models.EmailField()
    mail_subject = models.CharField(max_length=150)
    mail_body = models.TextField()

    request = models.ForeignKey(
        Request,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
