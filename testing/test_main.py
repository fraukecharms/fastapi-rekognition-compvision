from main import root
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app


def test_root():
    client = TestClient(app)
    response = client.get("/")

    assert response.status_code == 200


def test_labels():
    client = TestClient(app)

    response = client.post(
        "/labels",
        files={"photo": ("testpics/pic1.jpg", open("testpics/pic1.jpg", "rb"), "image/jpeg")},
    )

    assert response.status_code == 200

def test_draw_box():
    client = TestClient(app)

    response = client.post(
        "/draw_box",
        files={"photo": ("testpics/pic1.jpg", open("testpics/pic1.jpg", "rb"), "image/jpeg")},
    )
    print(response)

    assert response.status_code == 200
