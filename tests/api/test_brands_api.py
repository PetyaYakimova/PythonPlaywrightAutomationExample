import pytest


@pytest.mark.api
def test_get_all_brands(api_client):
    response = api_client.get("/brandsList")

    assert response.status_code == 200

    data = response.json()
    assert "brands" in data
    assert len(data["brands"]) > 0


@pytest.mark.api
def test_brands_in_products_exist_in_brands_list(api_client):
    brands_response = api_client.get("/brandsList")
    product_response = api_client.get("/productsList")

    brands = {b["brand"] for b in brands_response.json()["brands"]}
    products = product_response.json()["products"]

    for product in products:
        assert product["brand"] in brands
