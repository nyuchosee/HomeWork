import requests
import pytest
from pydantic import BaseModel
from typing import Optional

class Brewery(BaseModel):
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str]
    city: str
    state_province: Optional[str]
    postal_code: Optional[str]
    country: str
    phone: Optional[str]
    website_url: Optional[str]


# 1. **Тест получения списка пивоварен**
def test_get_all_breweries():
    url = "https://api.openbrewerydb.org/v1/breweries"
    response = requests.get(url)
    assert response.status_code == 200
    breweries = response.json()
    assert isinstance(breweries, list)
    assert len(breweries) > 0
    for brewery in breweries:
        Brewery(**brewery)


# 2. **Тест получения конкретной пивоварни по ID**
def test_get_brewery_by_id():
    brewery_id = "6d14b220-8926-4521-8d19-b98a2d6ec3db"  # Новый ID из API
    url = f"https://api.openbrewerydb.org/v1/breweries/{brewery_id}"
    response = requests.get(url)
    assert response.status_code == 200
    brewery = response.json()
    validated_brewery = Brewery(**brewery)
    assert validated_brewery.id == brewery_id


# 3. **Тест поиска пивоварен по городу (параметризация)**
@pytest.mark.parametrize("city", ["San Diego", "Denver", "Austin"])
def test_get_breweries_by_city(city):
    url = f"https://api.openbrewerydb.org/v1/breweries?by_city=Denver{city}"
    response = requests.get(url)
    assert response.status_code == 200
    breweries = response.json()
    assert isinstance(breweries, list)
    for brewery in breweries:
        Brewery(**brewery)
        assert brewery["city"].lower() == city.lower()  # Проверяем, что город совпадает


# 4. **Тест поиска пивоварен по типу (параметризация)**
@pytest.mark.parametrize("brewery_type", ["micro", "brewpub"])
def test_get_breweries_by_type(brewery_type):
    url = f"https://api.openbrewerydb.org/v1/breweries?by_type={brewery_type}"
    response = requests.get(url)
    assert response.status_code == 200
    breweries = response.json()
    assert isinstance(breweries, list)
    for brewery in breweries:
        Brewery(**brewery)
        assert brewery["brewery_type"] == brewery_type


# 5. **Тест поиска по названию пивоварни**
@pytest.mark.parametrize("name", ["Lagunitas", "Stone", "Dogfish"])
def test_search_breweries_by_name(name):
    url = f"https://api.openbrewerydb.org/v1/breweries/search?query={name}"
    response = requests.get(url)
    assert response.status_code == 200
    breweries = response.json()
    assert isinstance(breweries, list)
    for brewery in breweries:
        Brewery(**brewery)
    assert any(name.lower() in brewery["name"].lower() for brewery in breweries), f"Бренд {name} не найден в списке!"

