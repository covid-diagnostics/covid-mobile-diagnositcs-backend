from enum import Enum
from django.db import models
from django.contrib.postgres.fields import ArrayField

from api.models import User


class Genders(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NONBINARY = "NONBINARY"


class SmokingHabits(Enum):
    NEVER = "NEVER"
    STOPPED = "STOPPED"
    # RECENT = "RECENT"
    CURRENT = "CURRENT"


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(
        max_length=20,
        choices=[(g.value, g.value) for g in Genders],
        null=True,
        blank=True,
    )
    country = models.CharField(max_length=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    smoking_status = models.CharField(
        max_length=50, choices=[(g.value, g.value) for g in SmokingHabits], null=True
    )
    background_diseases = ArrayField(models.TextField(), null=True, blank=True)
