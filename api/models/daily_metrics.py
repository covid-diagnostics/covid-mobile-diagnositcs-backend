from django.db import models

from api.models import User


class DailyMetrics(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="submitted_metrics"
    )
    filled_on = models.DateTimeField(auto_now_add=True)

    temperature = models.DecimalField(max_digits=6, decimal_places=3)
    cough_strength = models.IntegerField()
    is_cough_dry = models.BooleanField()

    face_recording = models.FileField(null=True, blank=True)
    chest_recording = models.FileField(null=True, blank=True)

    FILE_FIELDS = ["face_recording", "chest_recording"]
