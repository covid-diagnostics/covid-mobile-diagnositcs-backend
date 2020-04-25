from enum import Enum
from django.db import models
from api.models import Question, Measurement


class QuestionResponse(models.Model):

    question = models.ForeignKey(
        Question, related_name="responses", on_delete=models.CASCADE
    )
    measurement = models.ForeignKey(
        Measurement, related_name="responses", on_delete=models.CASCADE
    )
    value = models.TextField(null=True, blank=True)
