import pytest
from app import create_app
from flask import current_app

@pytest.fixture
def app():
    app = create_app()
    #current_app.logger.info("In the test app")
    return app