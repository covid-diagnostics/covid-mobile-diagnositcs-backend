"""Serializers for the user models."""
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import EmailField

from api.models import User, UserQuestions


class UserSerializer(serializers.ModelSerializer):
    """(De)Serialize the user for easy serving with web api."""

    class Meta:
        # ref_name = "ApiUserSerializer"
        model = User
        exclude = [
            "password",
            "is_superuser",
            "is_staff",
            "groups",
            "user_permissions",
        ]
