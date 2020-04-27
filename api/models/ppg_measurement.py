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
    calibration_transform1 = models.TextField(null=True, blank=True)
    calibration_transform2 = models.TextField(null=True, blank=True)
    sensor_color_transform1 = models.TextField(null=True, blank=True)
    sensor_color_transform2 = models.TextField(null=True, blank=True)
    sensor_forward_matrix1 = models.TextField(null=True, blank=True)
    sensor_forward_matrix2 = models.TextField(null=True, blank=True)
    sensor_lens_shading_applied = models.BooleanField(null=True, blank=True)
    sensor_sensitivity_range_lower = models.IntegerField(null=True, blank=True)
    sensor_sensitivity_range_upper = models.IntegerField(null=True, blank=True)
    sensor_white_level = models.IntegerField(null=True, blank=True)
    sensor_max_analog_sensitivity = models.IntegerField(null=True, blank=True)
    sensor_reference_illuminant1 = models.IntegerField(null=True, blank=True)
    sensor_reference_illuminant2 = models.IntegerField(null=True, blank=True)

