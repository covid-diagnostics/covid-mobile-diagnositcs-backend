"""Views for Corona Testing API related to measurement intiation."""
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
from rest_framework.viewsets import ViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin

from api.models import Measurement
from api.serializers import MeasurementSerializer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


class MeasurementViewSet(CreateModelMixin, GenericViewSet):
    """Actions related to measurement creation and retreival"""

    permission_classes = [IsAuthenticated]
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    @swagger_auto_schema(
        operation_id="retrieveMeasurementCount", responses={200: openapi.TYPE_INTEGER}
    )
    @action(methods=["GET"], detail=False)
    def count(self, request):
        num_measurements = Measurement.objects.all().count()
        return Response(num_measurements)
