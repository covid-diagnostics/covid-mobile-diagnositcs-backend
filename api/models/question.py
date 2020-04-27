from enum import Enum
from django.db import models
from api.models import User


class QuestionType(Enum):
    CHECKBOX = "CHECKBOX"
    TEXT = "TEXT"
    MULTISELECT = "MULTISELECT"
    SELECT = "SELECT"
    RANGE = "RANGER"


class Question(models.Model):

    name = models.CharField(max_length=25)
    display_name = models.TextField()
    qtype = models.CharField(max_length=25, choices=[(q.value,q.value) for q in QuestionType])
    order = models.IntegerField()
    active = models.BooleanField(default=True)
    extra_data = models.TextField(blank=True, null=True)
    required = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        "Question",
        related_name="sub_questions",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name