from django.db import models
from django.contrib.postgres.fields import ArrayField

from api.models import Measurement


class PPGMeasurement(models.Model):

    measurement = models.ForeignKey(
        Measurement, on_delete=models.CASCADE, related_name="ppg_measurements"
    )
    red = ArrayField(models.FloatField())
    blue = ArrayField(models.FloatField())
    green = ArrayField(models.FloatField())
    timepoint = ArrayField(models.FloatField())
    phone_metadata = models.TextField(null=True, blank=True)
    