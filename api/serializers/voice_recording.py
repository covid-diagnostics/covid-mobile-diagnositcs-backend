"""Serializers for the ppg measurement models."""
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import EmailField

from api.models import VoiceRecording


class VoiceRecordingSerializer(serializers.ModelSerializer):
    """(De)Serialize the voice recording for easy serving with web api."""

    class Meta:
        # ref_name = "ApiUserSerializer"
        model = VoiceRecording
        fields = "__all__"

    def validate_measurement(self, measurement):
        user = self.context["request"].user
        if measurement.user != user:
            raise serializers.ValidationError(
                "This measurement doesn't belong to the user"
            )
        return measurement