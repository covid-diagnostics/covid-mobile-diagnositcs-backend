"""Serializers for the user models."""
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import EmailField

from api.models import User, UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    """(De)Serialize the user questionniers for easy serving with web api."""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        # ref_name = "ApiUserSerializer"
        model = UserInfo
        fields = "__all__"
