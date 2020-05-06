"""Views for Corona Testing API related to user actions."""
import logging
import random
from time import sleep

from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import DecimalField, F, Q
from django.db.models.functions import Power, Sqrt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action, api_view, permission_classes
from api.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from api.serializers import (
    UserSerializer,
    CreateUserSerializer,
    UserTokenSerializer,
    # DailyFilesSerializer,
    # DailyMetricsSerializer,
)

User = get_user_model()  # pylint: disable=invalid-name
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


class MeViewSet(ViewSet):
    """Actions the user performs on themselves"""

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_id="retrieveMe", responses={200: UserSerializer()})
    def list(self, request):
        """Simply returns a single user"""
        return Response(UserSerializer(request.user).data)

    @swagger_auto_schema(
        operation_id="userSignUp",
        method="POST",
        request_body=CreateUserSerializer(),
        responses={200: UserTokenSerializer()},
    )
    @action(methods=["POST"], detail=False, permission_classes=[AllowAny])
    def sign_up(self, request):
        """Signs up a user and returns the user and token"""
        ser = CreateUserSerializer(data=request.data)
        ser.is_valid(raise_exception=True)

        user = ser.save()

        return Response(UserTokenSerializer(user).data)
