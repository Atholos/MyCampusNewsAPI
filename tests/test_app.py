
from flask import url_for, Response
import pytest

# Testing basic app functionalities

@pytest.mark.options(debug=False)
def test_app(app):
    assert not app.debug, 'Ensure the app not in debug mode'
