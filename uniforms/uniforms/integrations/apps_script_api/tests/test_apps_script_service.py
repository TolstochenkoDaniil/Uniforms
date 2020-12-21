import pytest

from uniforms.integrations.apps_script_api import apps_script_service
from uniforms.integrations.apps_script_api.exceptions import NotRegisteredScript
from uniforms.integrations.apps_script_api.script import Parameter


@pytest.fixture
def service_response():
    return lambda name, params: apps_script_service.execute_script_by_name(script_name=name, args=params)


def test_apps_script_service_call(service_response):
    resp = service_response(
        'AssignTrigger2Form',
        [Parameter(name='url', value='https://docs.google.com/forms/d/1fRRrgd6y4m_VPHb-cB-f4GeCmSW6Uwz5tTry5qUN_iM/edit')]
    )

    assert resp.get('done') == True


@pytest.mark.parametrize('url', [
    'https://docs.google.com/forms/d/1fRRrgd6y4m_VPHb-cB-f4GeCmSW6Uwz5tTry5qUN_iM/edit', # use default url
    pytest.param('https://docs.google.com/forms/d/BaD_IdNUMber_101010_FaIL/edit', marks=pytest.mark.xfail)
])
def test_form_editor(service_response, url):
    resp = service_response(
        'CheckEditorPermission',
        [Parameter(name='url', value=url)]
    )

    assert resp.get('response').get('result') == True


def test_not_registered_script(service_response):
    with pytest.raises(NotRegisteredScript):
        service_response(
            'NotRegistered',
            Parameter(name='',value='')
        )