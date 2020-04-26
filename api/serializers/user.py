"""Serializers for the user models."""
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import EmailField

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    """(De)Serialize the user for easy serving with web api."""

    class Meta:
        # ref_name = "ApiUserSerializer"
        model = User
        fields = [
            "phonenumber_hash",
        ]


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["phonenumber_hash", "device_id"]
        # extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            phonenumber_hash=validated_data["phonenumber_hash"], device_id=validated_data["device_id"]
        )
        # user.set_password(validated_data["password"])
        user.save()
        return user
