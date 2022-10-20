from main import root
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_root():
    """
    curl -X 'GET'   'http://0.0.0.0:8080/showimage'   -H 'accept: application/json' --output streamimage.jpg
    """
    r = root()

    assert 1 == 1
