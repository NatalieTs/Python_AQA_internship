import json
from tests.user_helpers import prepare_user

def test_get_user_details_by_id(http_client, prepare_user):
    response = http_client.get(prepare_user)
    body = json.loads(response.text)
    assert len(body) > 0
    assert body['id'] == prepare_user
    assert response.status_code == 200


