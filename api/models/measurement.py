from uuid import uuid4
from django.db import models

from api.models import User


class Measurement(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="measurements"
    )
    filled_on = models.DateTimeField(auto_now_add=True)
    tag = models.UUIDField(default=uuid4)
