from tests.user_helpers import prepare_user
from tests import http_client


def test_delete_user(http_client, prepare_user):
    status_code, body = http_client.delete(prepare_user)

    assert status_code == 204

    status_code, body = http_client.get(prepare_user)

    assert status_code == 404

