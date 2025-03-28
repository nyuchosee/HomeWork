import requests
import pytest
from pydantic import BaseModel, ValidationError
from typing import Union, List

class DogApiResponse(BaseModel):
    message: Union[str, List[str]]  # message может быть строкой или списком строк
    status: str

BASE_URL = "https://dog.ceo/api/breeds/image/random"

# 1. Тест для получения случайного изображения собаки
def test_get_random_dog():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    try:
        data = DogApiResponse(**response.json())
        assert isinstance(data.message, str)
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации: {e}")

# 2. Тест для получения случайного изображения собаки по определенной породе
@pytest.mark.parametrize("breed", ["bulldog", "beagle", "poodle"])
def test_get_random_dog_by_breed(breed):
    url = f"https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    assert response.status_code == 200
    try:
        data = DogApiResponse(**response.json())
        assert isinstance(data.message, (str, list))
        if isinstance(data.message, list):
            assert all(isinstance(img, str) for img in data.message)
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации: {e}")

# 3. Тест на получение списка пород собак
def test_get_breeds_list():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert 'message' in data
    assert isinstance(data['message'], dict)

# 4. Тест для получения случайного изображения собаки
@pytest.mark.parametrize("breed", ["bulldog", "poodle", "terrier"])
def test_get_random_dog_image_for_breed(breed):
    url = f"https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    assert response.status_code == 200
    try:
        data = DogApiResponse(**response.json())
        assert 'message' in data.dict()
        assert isinstance(data.message, str)
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации: {e}")

# 5. Тест для получения случайных изображений собак по разным породам
@pytest.mark.parametrize("breed", ["bulldog", "beagle", "poodle"])
def test_get_multiple_random_dogs(breed):
    url = f"https://dog.ceo/api/breeds/image/random/{breed}"
    response = requests.get(url)
    assert response.status_code == 200
    try:
        data = DogApiResponse(**response.json())
        assert 'message' in data.dict()
        assert isinstance(data.message, (str, list))
        if isinstance(data.message, list):
            assert all(isinstance(img, str) for img in data.message)
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации: {e}")
