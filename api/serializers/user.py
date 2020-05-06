"""Serializers for the user models."""
from django.contrib.auth import get_user_model
from rest_framework import serializers
import bcrypt

from api.models import User

EXTRA_HASHES = 20


class UserSerializer(serializers.ModelSerializer):
    """(De)Serialize the user for easy serving with web api."""

    class Meta:
        # ref_name = "ApiUserSerializer"
        model = User
        fields = [
            "phone_number_hash",
            # "device_id",
        ]


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "phone_number_hash",
            # "device_id",
        ]
        # extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):

        user = User(
            phone_number_hash=validated_data["phone_number_hash"],
            # device_id=validated_data["device_id"],
        )

        # user.set_password(validated_data["password"])
        user.save()
        return user
