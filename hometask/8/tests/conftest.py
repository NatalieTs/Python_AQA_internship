import pytest

from tests.http_client import HttpClient
from tests.config import Config


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="test", help="test env name"
    )


@pytest.fixture(scope="session")
def http_client(request):
    env_name = request.config.getoption("--env")
    config = Config(env_name)
    base_url = config.base_url
    token = config.token
    users_path = config.users_path
    if not base_url or not token:
        raise Exception("BASE_URL or TOKEN is empty.")
    yield HttpClient(base_url, users_path, {'Authorization': f"Bearer {token}"})

