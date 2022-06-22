import json
from mimesis import Person


def test_create_user(http_client):
    person = Person('en')
    payload = {'name': 'Frau Müller',
               'email': person.email(),
               'gender': 'female',
               'status': 'inactive'}
    response = http_client.post(payload)

    body = json.loads(response.text)
    body.pop("id")
    assert response.status_code == 201
    assert payload == body

