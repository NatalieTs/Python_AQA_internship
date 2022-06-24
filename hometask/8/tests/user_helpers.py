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
    status_code, body = http_client.post(payload)

    yield body.pop("id")

