import uuid
from datetime import timedelta, datetime

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
    username = models.CharField(max_length=20, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.username


class PasswordResetRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)
    reset_token = models.UUIDField(null=True, blank=True, unique=True)

    def is_expired(self):
        expiration_time = self.created_at + timedelta(minutes=10)
        return datetime.now(self.created_at.tzinfo) > expiration_time

    def __str__(self):
        return f"ResetRequest for {self.user.username} ({self.token})"
