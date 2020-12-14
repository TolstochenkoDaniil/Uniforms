import pytest
from google_api_client.services import ServiceProvider


@pytest.fixture
def request_body():
    request = {
        "function": "AssignTrigger2Form",
        "parameters": [{
            "url": 'https://docs.google.com/forms/d/1fRRrgd6y4m_VPHb-cB-f4GeCmSW6Uwz5tTry5qUN_iM/edit'
        }],
        "devMode":True
    }
    return request


@pytest.fixture
def script_id():
    SCRIPT_ID = '1Es4B6fDpiq9EfmPUtnWtxRWZE45-CquQzucmGFkL4GI8hkcWB0dB8DXw'
    
    return SCRIPT_ID


def test_apps_script_service_call(request_body, script_id):
    service = ServiceProvider().get_service()
    service.execute_script(request_body, script_id)
    resp = service.response
    
    assert resp.get('done') == True