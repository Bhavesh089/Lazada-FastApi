from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_getToken():
    response = client.post(
        '/CreateToken/0_121585_LRdFX8FyDbmggi92R9uK5DN41341')
    print(response)
    assert response.status_code == 200


def test_bad_getToken():
    response = client.post(
        '/CreateToken/ascianoiascm')
    assert response.status_code == 400


def test_invalid_getToken():
    response = client.post('/CreateToken/hrdsfn/helloworld')
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Not Found"
    }
