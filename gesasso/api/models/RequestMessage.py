from django.db.models import AutoField, TextField, BooleanField, ForeignKey, CASCADE

from gesasso.api.models import Request
from gesasso.api.utils import TimeStampable


class RequestMessage(TimeStampable):
    id = AutoField(primary_key=True)
    request = ForeignKey(Request, on_delete=CASCADE)
    message = TextField()
    # user = ForeignKey("User", on_delete=CASCADE)
    internal = BooleanField(default=False)
