import json

import pytest
from mimesis import Person


@pytest.fixture(scope="function")
def prepare_user(http_client):
    person = Person('en')
    payload = {'name': 'Frau Müller',
               'email': person.email(),
               'gender': 'female',
               'status': 'inactive'}
    response = http_client.post("/public/v2/users", payload)

    body = json.loads(response.text)
    yield body.pop("id")

