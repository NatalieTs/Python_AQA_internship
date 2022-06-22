import json

import fixture as fixture
import pytest

from tests.user_helpers import prepare_user


def test_update_user_details(http_client, prepare_user):
    payload = {'name': 'Senior X'}
    response = http_client.put(prepare_user, payload=payload)
    body = json.loads(response.text)
    assert response.status_code == 200
    assert body['name'] == payload['name']

