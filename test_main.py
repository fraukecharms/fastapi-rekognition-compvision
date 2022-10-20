from main import root
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app


def test_root():
    client = TestClient(app)
    response = client.get("/")

    assert response.status_code == 200
    # assert response.json() == {"msg": "Hello World"}


def test_labels():
    client = TestClient(app)

    response = client.post(
        "/labels",
        files={"photo": ("filename", open("testpic/pic1.jpg", "rb"), "image/jpeg")},
    )

    assert response.status_code == 200
