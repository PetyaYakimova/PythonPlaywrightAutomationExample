import pytest


@pytest.mark.api
def test_search_product(api_client):
    payload = {
        "search_product": "top"
    }

    response = api_client.post(
        "/searchProduct",
        data=payload
    )

    assert response.status_code == 200

    data = response.json()
    assert "products" in data
    assert len(data["products"]) > 0
