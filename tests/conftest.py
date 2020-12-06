import pytest
import os
from app import create_app
from flask import current_app

@pytest.fixture
def app():
    os.environ["APP_CONFIG"] = "../config/test.py"
    print(os.environ["APP_CONFIG"])
    app = create_app()
    return app