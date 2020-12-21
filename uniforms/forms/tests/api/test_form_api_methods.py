import pytest

from forms.models import Form

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def form(mixer, user):
    return mixer.blend('forms.Form', name='Test', url='goo.text.com', discipline='CS', user_id=str(user.id))


@pytest.fixture
def form_params(form):
    params = dict(
        name=form.name,
        url=form.url,
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