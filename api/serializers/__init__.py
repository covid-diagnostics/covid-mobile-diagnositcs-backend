"""Serializers for the corona_testing API."""
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .auth import UserTokenSerializer

from .user import UserSerializer, CreateUserSerializer

from .question import QuestionSerializer
from .measurement import MeasurementSerializer
from .question_response import QuestionResponseSerializer
from .voice_recording import VoiceRecordingSerializer
from .ppg_measurement import PPGMeasurementSerializer

from .user_info import UserInfoSerializer
