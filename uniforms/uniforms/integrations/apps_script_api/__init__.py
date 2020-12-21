from uniforms.integrations.apps_script_api.service import ServiceProvider
from uniforms.integrations.apps_script_api.script import scripts


apps_script_service = ServiceProvider().get_service()
apps_script_service.register(scripts)

__all__ = [
    apps_script_service
]