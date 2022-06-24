from tests.user_helpers import prepare_user


def test_update_user_details(http_client, prepare_user):
    payload = {'name': 'Senior X'}
    status_code, body = http_client.put(prepare_user, payload=payload)

    assert status_code == 200
    assert body['name'] == payload['name']

