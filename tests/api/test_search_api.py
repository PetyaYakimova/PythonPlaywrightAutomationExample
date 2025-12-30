import pytest
import requests


@pytest.mark.api
def test_search_product(api_base_url):
    payload = {
        "search_product": "top"
    }

    response = requests.post(
        f"{api_base_url}/searchProduct",
        data=payload
    )

    assert response.status_code == 200

    data = response.json()
    assert "products" in data
    assert len(data["products"]) > 0
