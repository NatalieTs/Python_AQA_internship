def test_get_user_details(http_client):
    status_code, body = http_client.get()

    assert len(body) > 0
    assert status_code == 200


