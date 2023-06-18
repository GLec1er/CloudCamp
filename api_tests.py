import requests
import pytest

API_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.parametrize("params", [
    {},
    {"userId": 1},
    {"id": 1},
    {"title": "sunt aut facere repellat"},
    {"body": "quia et suscipit\nsuscipit recusandae consequuntur"},
])
def test_get_posts(params):
    response = requests.get(f"{API_URL}/posts", params=params)
    assert response.status_code == 200
    # Добавьте дополнительные проверки для ответа, если необходимо

def test_post_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(f"{API_URL}/posts", json=payload)
    assert response.status_code == 201
    # Добавьте дополнительные проверки для ответа, если необходимо

def test_delete_post():
    response = requests.delete(f"{API_URL}/posts/1")
    assert response.status_code == 200
