import time

import pytest
from unittest.mock import patch

from forms.tasks import check_form_edit_permission


pytestmark = [pytest.mark.django_db]


@pytest.fixture
def form(mixer, user):
    return mixer.blend(
        'forms.Form',
        name='Test',
        url='goo.text.com',
        edit_url='https://docs.google.com/forms/d/1fRRrgd6y4m_VPHb-cB-f4GeCmSW6Uwz5tTry5qUN_iM/edit',
        discipline='CS',
        user_id=str(user.id)
    )


@pytest.fixture
def form_params(form):
    params = dict(
        name='New Title',
        url=form.url,
        edit_url=form.edit_url,
        university=form.university,
        discipline=form.discipline
    )
    return params


@pytest.fixture
def task_args():
    return 'qwertyuio3456', 'http://test.com/EDIT'


def test_task_run(celery_worker, task_args):
    assert check_form_edit_permission.delay(*task_args)


@patch('forms.tasks.check_form_edit_permission.run')
def test_mock_task_run(mock_run, task_args):
    assert check_form_edit_permission.run(*task_args)
    check_form_edit_permission.run.assert_called_once_with(*task_args)

    assert check_form_edit_permission.run(*task_args)
    assert check_form_edit_permission.run(*task_args)
    check_form_edit_permission.run.call_count == 2


@pytest.mark.django_db(transaction=True)
def test_check_permission_task(api, user, form, celery_worker):
    resp = api.get(f'/api/v1/{user.get_id}/form')

    id = resp.get('form_params').get('id')
    url = resp.get('form_params').get('edit_url')

    result = check_form_edit_permission.delay(id, url).get()
    assert result.get('result') == True

    resp = api.get(f'/api/v1/{user.get_id}/form')

    assert resp.get('form_params').get('is_valid') == True