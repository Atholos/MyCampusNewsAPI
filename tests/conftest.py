import pytest
from app import APP


@pytest.fixture
def app():
    myapp = APP
    return myapp