from flask import url_for, Response
import pytest

def test_home(client):
    res = client.get(url_for("home"))
    assert res.json() == {"Home": "Home"}

def test_home2(client):
    res = client.get(url_for("home"))
    print(res)
    assert res.status_code == 200

def test_homenot(client):
    res = client.post(url_for("home"))
    assert res is not None
