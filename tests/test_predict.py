
from flask import url_for, Response
import pytest

body = {
    "petal_length": 4,
    "sepal_length": 4,
    "petal_width": 1,
    "sepal_width": 2
}

@pytest.mark.options(debug=False)
def test_app(app):
    assert not app.debug, 'Ensure the app not in debug mode'

def test_predictnot(client):
    res = client.post(url_for("predict"), data=body)
    assert res is not None

def test_predictrandom(client):
    res = client.post(url_for("predict"), data=body)
    assert res != "Random words"

def test_predict(client):
    res = client.post(url_for("predict"), data=body)
    assert res == "iris-setosa" or "iris-versicolor" or "iris-virginica"
