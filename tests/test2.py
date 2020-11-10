from flask import url_for, Response
import pytest

body = {
    "petal_length": 2,
    "sepal_length": 2,
    "petal_width": 3,
    "sepal_width": 2
}

def test_predictnot(client):
    res = client.post(url_for("predict"), data=body)
    assert res is not None