from mimesis import Person


def test_create_user(http_client):
    person = Person('en')
    payload = {'name': 'Frau Müller',
               'email': person.email(),
               'gender': 'female',
               'status': 'inactive'}
    status_code, body = http_client.post(payload)
    body.pop("id")
    assert status_code == 201
    assert payload == body

