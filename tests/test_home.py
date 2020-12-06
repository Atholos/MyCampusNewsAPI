from flask import url_for, Response
import pytest

#Testing home, url_for finds the localhost for you

def test_home(client):
    res = client.get(url_for("home"))
    assert res != "Home"

# Note = tests use the actual route functions instead of routes like "/home"

def test_home2(client):
    res = client.get(url_for("home"))
    print(res)
    assert res.status_code == 200

def test_homenot(client):
    res = client.get(url_for("home"))
    assert res is not None