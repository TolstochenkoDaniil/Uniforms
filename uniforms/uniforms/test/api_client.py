import json
import random
import string

from mixer.backend.django import mixer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient


class DRFClient(APIClient):

    def __init__(self, user=None, god_mode=True, anon=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not anon:
            self.auth(user, god_mode)

    def auth(self, user=None, god_mode=True):
        self.user = user or self._create_user(god_mode)
        self.god_mode = god_mode

        token = RefreshToken.for_user(self.user)
        self.credentials(
            HTTP_AUTHORIZATION=f'Bearer {token}',
            HTTP_X_GM_CLIENT='testing',
        )

    def _create_user(self, god_mode=True):
        user_opts = dict()

        if god_mode:
            user_opts = {
                'is_stuff': False,
                'is_superuser': True,
            }
        user = mixer.blend('social_auth.UniformsUser', **user_opts)
        self.password = ''.join([random.choice(string.hexdigits) for _ in range(0, 6)])
        user.set_password = self.password
        user.save()

        return user

    def logout(self):
        self.credentials()
        super().logout()

    def get(self, *args, **kwargs):
        return self._api_call('get', kwargs.get('expected_status_code', 200), *args, **kwargs)

    def post(self, *args, **kwargs):
        return self._api_call('post', kwargs.get('expected_status_code', 201), *args, **kwargs)

    def put(self, *args, **kwargs):
        return self._api_call('put', kwargs.get('expected_status_code', 200), *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self._api_call('delete', kwargs.get('expected_status_code', 204), *args, **kwargs)

    def _api_call(self, method, expected, *args, **kwargs):
        kwargs['format'] = kwargs.get('format', 'json')
        as_response = kwargs.pop('as_response', False)

        method = getattr(super(), method)
        response = method(*args, **kwargs)

        if as_response:
            return response

        content = self._decode(response)

        assert response.status_code == expected, content

        return content

    def _decode(self, response):
        if not len(response.content):
            return

        content = response.content.decode('utf-8', errors='ignore')

        if 'application/json' in response._headers['content-type'][1]:
            return json.loads(content)
        else:
            return content