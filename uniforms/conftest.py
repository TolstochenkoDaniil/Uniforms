import pytest

from uniforms.test.api_client import DRFClient
from mixer.backend.django import mixer as _mixer


@pytest.fixture
def api():
    return DRFClient()


@pytest.fixture
def anon():
    return DRFClient(anon=True)


@pytest.fixture
def mixer():
    return _mixer

@pytest.fixture
def user(mixer):
    return mixer.blend('social_auth.UniformsUser')