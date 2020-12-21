from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class UniformsUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    is_premium = models.BooleanField(
        default=False,
        editable=True,
        verbose_name='User paid status'
    )
    is_banned = models.BooleanField(
        default=False,
        editable=True,
        verbose_name='User access status'
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user_table'
        verbose_name_plural = 'users_table'

    @property
    def get_id(self):
        return str(self.id).replace('-', '')