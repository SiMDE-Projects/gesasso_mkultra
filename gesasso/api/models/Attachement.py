from django.db import models

from gesasso.api.utils import TimeStampable


class Attachement(TimeStampable):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    type = models.TextField()
    data = models.FileField(upload_to="attachements")
    request_message = models.ForeignKey(
        "RequestMessage", on_delete=models.CASCADE, related_name="attachements"
    )
