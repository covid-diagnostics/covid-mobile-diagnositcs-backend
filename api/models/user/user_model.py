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
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property


class HashedUserManager(UserManager):
    def _create_user(self, phone_number_hash, email, password, **extra_fields):
        """
        Create and save a user with the given hashed id, email, and password.
        """
        email = self.normalize_email(email)
        #username = self.model.normalize_username(username)
        user = self.model(phone_number_hash=phone_number_hash, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number_hash, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number_hash, email, password, **extra_fields)

    def create_superuser(self, phone_number_hash, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number_hash, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom Corona Testing user implementation
    """

    username_validator = UnicodeUsernameValidator()

    phone_number_hash = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128, null=True,blank=True)
    email = models.EmailField(null=True, blank=True)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False, 
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = HashedUserManager()

    USERNAME_FIELD = "phone_number_hash"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number_hash
