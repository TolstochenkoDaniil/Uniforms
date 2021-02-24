import pytest

from forms.models import FormStatus


pytestmark = [pytest.mark.django_db]


@pytest.fixture
def form(mixer, user):
    return mixer.blend('forms.Form', name='Test', url='goo.text.com', user_id=str(user.id))


def test_create_form(form):
    assert form is not None
    assert 'Test' in str(form)


def test_status_after_create(form):
    assert form.is_valid == False


@pytest.mark.parametrize('status', [
    FormStatus.COMMON,
    FormStatus.PREMIUM,
    FormStatus.BANNED,
])
def test_form_change_status(form, status):
    form.change_status(status)

    assert form.status == status