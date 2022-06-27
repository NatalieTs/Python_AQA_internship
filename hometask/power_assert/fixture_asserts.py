import pytest
from power_assert import PowerAssert


@pytest.fixture(scope="session")
def soft_assert():
    return PowerAssert(softly=True)


@pytest.fixture(scope="session")
def hard_assert():
    return PowerAssert(softly=False)


