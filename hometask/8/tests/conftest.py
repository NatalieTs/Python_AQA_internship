import pytest

from tests.http_client import HttpClient
from tests.config import Config


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="local", help="env variable name"
    )


@pytest.fixture(scope="session")
def http_client(request):
    env_name = request.config.getoption("--env")
    config = Config(env_name)
    base_url = config.base_url
    token = config.token
    if not base_url or not token:
        raise Exception("BASE_URL or TOKEN is empty.")
    yield HttpClient(base_url, {'Authorization': f"Bearer {token}"})

