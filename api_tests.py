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
    # Добавьте дополнительные проверки для ответа, если необходимо

def test_get_post_by_id():
    response = requests.get(f"{API_URL}/posts/1")
    assert response.status_code == 200
    # Добавьте дополнительные проверки для ответа, если необходимо

def test_get_comments_by_post_id():
    response = requests.get(f"{API_URL}/posts/1/comments")
    assert response.status_code == 200
    # Добавьте дополнительные проверки для ответа, если необходимо

def test_update_post():
    payload = {
        "title": "foo",
        "body": "bar",
    }
    response = requests.put(f"{API_URL}/posts/1", json=payload)
    assert response.status_code == 200
    # Добавьте дополнительные проверки для ответа, если необходимо

def test_patch_post():
    payload = {
        "title": "foo",
    }
    response = requests.patch(f"{API_URL}/posts/1", json=payload)
    assert response.status_code == 200
    # Добавьте дополнительные проверки для ответа, если необходимо

def test_get_users():
    response = requests.get(f"{API_URL}/users")
    assert response.status_code == 200
    # Добавьте дополнительные проверки для ответа, если необходимо

def test_get_user_by_id():
    response = requests.get(f"{API_URL}/users/1")
    assert response.status_code == 200
    # Добавьте дополнительные проверки для ответа, если необходимо

def test_post_user():
    payload = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john@example.com"
    }
    response = requests.post(f"{API_URL}/users", json=payload)
    assert response.status_code == 201
