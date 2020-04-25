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
from rest_framework.viewsets import ViewSet, ReadOnlyModelViewSet

from api.models import Question
from api.serializers import QuestionSerializer

User = get_user_model()  # pylint: disable=invalid-name
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


class QuestionViewSet(ReadOnlyModelViewSet):
    """Actions the user performs on themselves"""

    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()
