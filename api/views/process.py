"""Views for Corona Testing API related to processing inputs actions."""
import logging
import random
from random import randint
from time import sleep

from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import DecimalField, F, Q
from django.db.models.functions import Power, Sqrt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from api.serializers import HeartRateRecordingSerializer, HeartRateSerializer

User = get_user_model()  # pylint: disable=invalid-name
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


class ProcessViewSet(ViewSet):
    """Actions the user performs on themselves"""

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="processHeartRate",
        method="POST",
        request_body=HeartRateRecordingSerializer(),
        responses={200: HeartRateSerializer()},
    )
    @action(methods=["POST"], detail=False, permission_classes=[AllowAny])
    def heart_rate(self, request):
        """Signs up a user and returns the user and token"""
        ser = HeartRateRecordingSerializer(data=request.data)
        ser.is_valid(raise_exception=True)

        rate = randint(55, 85)
        sat_rate = randint(84, 96)
        return Response({"heartRate": rate, "saturationPercentage": sat_rate})
