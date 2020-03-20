from django.db import models

from api.models import User


class UserQuestions(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="filled_questions"
    )
    filled_on = models.DateField(auto_now_add=True)

    temperature = models.DecimalField(max_digits=6, decimal_places=3)
    cough_strength = models.IntegerField()
    is_cough_dry = models.BooleanField()
