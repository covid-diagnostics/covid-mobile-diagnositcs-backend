"""Serializers for the ppg measurement models."""
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import EmailField

from api.models import QuestionResponse


class QuestionResponseSerializer(serializers.ModelSerializer):
    """(De)Serialize the ppg measurement for easy serving with web api."""

    class Meta:
        # ref_name = "ApiUserSerializer"
        model = QuestionResponse
        fields = "__all__"

    def validate_measurement(self, measurement):
        user = self.context["request"].user
        if measurement.user != user:
            raise serializers.ValidationError(
                "This measurement doesn't belong to the user"
            )
        return measurement