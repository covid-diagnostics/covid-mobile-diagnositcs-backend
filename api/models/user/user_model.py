# pylint: disable=missing-docstring
"""Models related to user functionality and data."""
from __future__ import annotations

import logging
import os
from datetime import datetime, timedelta
from random import SystemRandom
from typing import TYPE_CHECKING, Any, Dict, Optional, List
from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property

# from django_fsm import FSMKeyField, transition
# from phonenumber_field.modelfields import PhoneNumberField

# import api.sms

# from api.util import get_base_url

# from ..category_attributes import CategoryAttributeEnum
# from ..status import OnboardingEnum, ProviderRequestEnum, UserEnum
# from ..user_requests import ProviderRequest
# from .exceptions import *  # pylint: disable=wildcard-import, unused-wildcard-import
# from .onboarding.onboarding_verifier import OnboardingVerifier
# from .user_email import UserEmail

# if TYPE_CHECKING:
#     from api.models import Address, UserChangeRequest, ServiceProviderCategory
#     from django.db.models.query import QuerySet  # pylint: disable= ungrouped-imports

# logger = logging.getLogger(__name__)  # pylint: disable=invalid-name
# logger.setLevel(logging.INFO)

# BYPASS_NUMBER = "+447333090909"

# ONOBARDING_STATES = [status.value for status in OnboardingEnum]


# class UserStatus(models.Model):
#     id = models.CharField(max_length=100, unique=True, primary_key=True)

#     def __str__(self):
#         return self.id

#     @classmethod
#     def get_status(cls, status):
#         return cls.objects.get(status=status)

#     class Meta:
#         verbose_name_plural = "User statuses"


class User(AbstractUser):
    """Custom Corona Testing  user implementation
    """

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=25, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: List[str] = []
