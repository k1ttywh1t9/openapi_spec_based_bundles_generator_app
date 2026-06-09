import pytest
from punq import Container
from logic.init_container import init_container


@pytest.fixture
def container() -> Container:
    """Fixture that gives isolated container for each test."""
    return init_container()
