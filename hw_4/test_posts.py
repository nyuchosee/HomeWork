import requests
import pytest
from pydantic import BaseModel, ValidationError

class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# 1. Тест для получения всех постов
def test_get_all_posts():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    try:
        for post in data:
            Post(**post)
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации: {e}")

# 2. Тест для получения поста по ID
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_post_by_id(post_id):
    url = f"{BASE_URL}/{post_id}"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    try:
        post = Post(**data)
        assert isinstance(post.title, str)
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации: {e}")

# 3. Тест на создание нового поста (POST запрос)
def test_create_post():
    url = BASE_URL
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data['title'] == payload['title']

# 4. Тест на получение поста по несуществующему ID
def test_get_invalid_post():
    url = f"{BASE_URL}/99999"
    response = requests.get(url)
    assert response.status_code == 404

# 5. Тест на фильтрацию постов по пользователю
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_posts_by_user(user_id):
    url = f"{BASE_URL}?userId={user_id}"
    response = requests.get(url)
    assert response.status_code