from django.db import models
from django.conf import settings
import uuid

from forms.tasks import check_form_edit_permission


class FormStatus(models.IntegerChoices):
    COMMON = 0
    PREMIUM = 1
    BANNED = -1


class Form(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        auto_created=True,
        editable=False,
        verbose_name='Form\'s GUID'
    )
    name = models.TextField(
        null=True,
        blank=False,
        max_length=80,
        editable=True,
        verbose_name='Form name',
        error_messages={
            'blank':'Name could\'not be empty'
        }
    )
    url = models.URLField(
        null=True,
        blank=False,
        editable=True,
        error_messages={
            'blank':'URL could\'not be empty'
        },
        verbose_name='URL from google forms'
    )
    edit_url = models.URLField(
        null=True,
        blank=False,
        editable=True,
        error_messages={
            'blank':'Edit URL could not be empty'
        },
        verbose_name='URL for editing google forms'
    )
    university = models.CharField(
        null=True,
        blank=False,
        max_length=40,
        error_messages={
            'blank':'University could not be empty'
        },
        verbose_name='User\'s university'
    )
    discipline = models.CharField(
        null=True,
        blank=False,
        editable=True,
        max_length=40,
        error_messages={
            'blank':'Discipline could not be empty'
        },
        verbose_name='Discipline name that form refers to'
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user',
        verbose_name='Form\'s owner id'
    )
    creation_date = models.DateTimeField(
        null=True,
        blank=False,
        editable=False,
        auto_now_add=True,
        verbose_name='Time stamp of creating/editing form'
    )
    modified = models.DateTimeField(
        null=True,
        blank=False,
        editable=True,
        auto_now=True,
        verbose_name='Time when form was last modified'
    )
    status = models.IntegerField(
        choices=FormStatus.choices,
        default=FormStatus.COMMON,
        editable=True,
        verbose_name='Form status'
    )
    is_valid = models.BooleanField(
        default=False,
        auto_created=True,
        editable=True,
        verbose_name='Does the form have edit permissions'
    )

    class Meta:
        db_table = 'forms'
        indexes = [
            models.Index(fields=['creation_date'], name='creation_date_idx'),
        ]
        ordering = ['status', 'creation_date']

    def __str__(self):
        return f'Form "{self.name}"'

    def change_status(self, status):
        self.status = status
        self.save()

    def check_edit_permission(self):
        if self.status != FormStatus.BANNED:
            check_form_edit_permission.delay(self.id, self.edit_url)