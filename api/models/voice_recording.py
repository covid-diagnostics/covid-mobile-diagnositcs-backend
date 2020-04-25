from django.db import models
from django.contrib.postgres.fields import ArrayField

from api.models import Measurement


class VoiceRecording(models.Model):

    measurement = models.ForeignKey(
        Measurement, on_delete=models.CASCADE, related_name="submitted_voice_recordings"
    )
    recording_file = models.FileField(null=True, blank=True)
    recording_metadata = models.TextField(null=True, blank=True)
