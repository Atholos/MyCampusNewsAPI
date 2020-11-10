
from flask import url_for, Response
import pytest

'''
url = 'http://127.0.0.1:1080/predict'  # localhost and the defined port + endpoint

response = requests.post(url, data=body)
print(response.json())


def test_petal():
    print("Test petal")
    assert response.json() == "iris-setosa" or "iris-versicolor" or 'iris-virginica'
'''

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

def test_predict(client):
    res = client.post(url_for("predict"), data=body)
    assert res == "iris-setosa" or "iris-versicolor" or "iris-virginica"
