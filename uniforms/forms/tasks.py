from django.apps import apps
from uniforms.celery import celery

from uniforms.integrations.apps_script_api import apps_script_service
from uniforms.integrations.apps_script_api.script import Parameter


@celery.task
def check_form_edit_permission(form_id, edit_url):
    response = apps_script_service.execute_script_by_name(
        script_name='CheckEditorPermission',
        args=[Parameter(name='url',value=edit_url)]
    )

    if response.get('response').get('result'):
        form = apps.get_model('forms.Form').objects.filter(pk=form_id).get()
        form.is_valid = True
        form.save()
    
    return response.get('response')