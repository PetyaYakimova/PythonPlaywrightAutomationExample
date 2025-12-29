import pytest
import requests


@pytest.mark.api
def test_get_all_products(api_base_url):
    response = requests.get(f"{api_base_url}/productsList")

    assert response.status_code == 200

    data = response.json()
    assert data is not None
