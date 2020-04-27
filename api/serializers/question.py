"""Serializers for the ppg measurement models."""
import json
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import EmailField

from api.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """(De)Serialize the ppg measurement for easy serving with web api."""

    json_extra_data = serializers.SerializerMethodField()

    class Meta:
        # ref_name = "ApiUserSerializer"
        model = Question
        fields = [
            "name",
            "display_name",
            "qtype",
            "order",
            "active",
            "extra_data",
            "required",
            "added_on",
            "json_extra_data",
        ]

    def get_json_extra_data(self, obj):
        try:
            return json.loads(obj.extra_data)
        except Exception as e:
            return ""
