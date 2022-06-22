import json
from tests import http_client


def test_cant_create_user_with_blank_email(http_client):
    payload = {'name': 'Frau Müller',
               'email': '',
               'gender': 'female',
               'status': 'inactive'}
    response = http_client.post(payload)

    body = json.loads(response.text)
    assert response.status_code == 422
    assert body[0]['message'] == "can't be blank"
