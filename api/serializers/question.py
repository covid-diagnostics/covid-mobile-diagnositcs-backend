"""Serializers for the ppg measurement models."""
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import EmailField

from api.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """(De)Serialize the ppg measurement for easy serving with web api."""

    class Meta:
        # ref_name = "ApiUserSerializer"
        model = Question
        fields = "__all__"
