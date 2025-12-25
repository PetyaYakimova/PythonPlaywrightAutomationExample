import pytest
import requests

BASE_API_URL = "https://automationexercise.com/api"


@pytest.mark.api
# Test API
def test_get_all_products():
    response = requests.get(f"{BASE_API_URL}/productsList")

    assert response.status_code == 200

    data = response.json()
    assert data is not None
