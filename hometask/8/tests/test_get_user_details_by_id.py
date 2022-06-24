import json
from tests.user_helpers import prepare_user

def test_get_user_details_by_id(http_client, prepare_user):
    status_code, body = http_client.get(prepare_user)
    assert len(body) > 0
    assert body['id'] == prepare_user
    assert status_code == 200


