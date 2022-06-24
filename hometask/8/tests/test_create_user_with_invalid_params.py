import json
from tests import http_client


def test_cant_create_user_with_blank_email(http_client):
    payload = {'name': 'Frau Müller',
               'email': '',
               'gender': 'female',
               'status': 'inactive'}
    status_code, body = http_client.post(payload)

    assert status_code == 422
    assert body[0]['message'] == "can't be blank"
