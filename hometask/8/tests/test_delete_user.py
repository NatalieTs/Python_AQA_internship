from tests.user_helpers import prepare_user
from tests import http_client


def test_delete_user(http_client, prepare_user):
    response = http_client.delete(prepare_user)

    assert response.status_code == 204

    response = http_client.get(prepare_user)

    assert response.status_code == 404

