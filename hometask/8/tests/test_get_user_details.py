import json


def test_get_user_details(http_client):
    response = http_client.get(f"/public/v2/users/")
    body = json.loads(response.text)
    assert len(body) > 0
    assert response.status_code == 200


