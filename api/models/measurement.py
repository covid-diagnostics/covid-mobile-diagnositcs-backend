from uuid import uuid4
from enum import Enum

from django.db import models

from api.models import User


class UserFeeling(Enum):
    SAME = "SAME"
    BETTER = "BETTER"
    WORSE = "WORSE"


class Measurement(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="measurements"
    )
    filled_on = models.DateTimeField(auto_now_add=True)
    tag = models.UUIDField(default=uuid4)

    temp_measurement = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    exposure_date = models.DateField(blank=True, null=True)
    positive_test_date = models.DateField(blank=True, null=True)
    negative_test_date = models.DateField(blank=True, null=True)
    general_feeling = models.CharField(
        max_length=10, choices=[(e.value, e.value) for e in UserFeeling], null=True
    )
