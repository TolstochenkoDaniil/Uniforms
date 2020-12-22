import pytest
import time

from forms.models import Form
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
        name=form.name,
        url=form.url,
        edit_url=form.edit_url,
        university=form.university,
        discipline=form.discipline
    )
    return params


def test_update_form_endpoint(api, user, form_params):
    resp = api.post(f'/api/v1/{user.get_id}/form', form_params)

    assert resp.get('status') == 'updated'


def test_create_form_endpoint(api, user, form_params):
    Form.objects.filter(user_id__exact=user.get_id).delete()
    resp = api.post(f'/api/v1/{user.get_id}/form', form_params)

    assert resp.get('status') == 'created'


def test_list_form_endpoint(api, form):
    resp = api.get(f'/api/v1/forms/{form.discipline}/list')

    assert resp[0].get('name') == form.name


def test_retrieve_form_endpoint(api, user, form):
    resp = api.get(f'/api/v1/{user.get_id}/form')

    assert resp.get('form_params').get('name') == form.name
    assert resp.get('form_params').get('url') == form.url
    assert resp.get('form_params').get('edit_url') == form.edit_url
    assert resp.get('form_params').get('discipline') == form.discipline
    assert resp.get('form_params').get('is_valid') == form.is_valid


def test_check_permission_task(api, user):
    resp = api.get(f'/api/v1/{user.get_id}/form')

    id = resp.get('form_params').get('id')
    url = resp.get('form_params').get('edit_url')

    check_form_edit_permission.delay(form_id=id, edit_url=url)

    time.sleep(10)

    resp = api.get(f'/api/v1/{user.get_id}/form')

    assert resp.get('form_params').get('is_valid') == True