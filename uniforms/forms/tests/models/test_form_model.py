import pytest

from forms.models import Form


pytestmark = [pytest.mark.django_db]


@pytest.fixture
def form(mixer, user):
    return mixer.blend('forms.Form', name='Test', url='goo.text.com', user_id=str(user.id))


def test_create_form(form):
    assert form is not None
    assert 'Test' in str(form)


@pytest.mark.parametrize('status', [
    Form.FORM_STATUS.COMMON,
    Form.FORM_STATUS.PREMIUM,
    Form.FORM_STATUS.BANNED,
])
def test_form_change_status(form, status):
    form.change_status(status)

    assert form.status == status