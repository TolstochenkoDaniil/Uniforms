from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import transaction

from forms.models import Form
from forms.tasks import check_form_edit_permission


@receiver(post_save, sender=Form)
def check_editor_permisson(sender, instance, **kwargs):
    transaction.on_commit(
        lambda: check_form_edit_permission.apply_async(args=(instance.id, instance.edit_url))
    )