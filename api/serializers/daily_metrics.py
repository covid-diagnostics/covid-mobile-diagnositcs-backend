"""Serializers for the user models."""
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import EmailField

from api.models import User, DailyMetrics


class DailyMetricsSerializer(serializers.ModelSerializer):
    """(De)Serialize the user questionniers for easy serving with web api."""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        # ref_name = "ApiUserSerializer"
        model = DailyMetrics
        exclude = DailyMetrics.FILE_FIELDS


class DailyFilesSerializer(serializers.ModelSerializer):
    class Meta:
        # ref_name = "ApiUserSerializer"
        model = DailyMetrics
        fields = DailyMetrics.FILE_FIELDS + ["id"]


class HeartRateRecordingSerializer(serializers.Serializer):
    finger_video = serializers.FileField()


class HeartRateSerializer(serializers.Serializer):
    heart_rate = serializers.IntegerField()
    saturation_percentage = serializers.DecimalField(max_digits=4, decimal_places=2)
