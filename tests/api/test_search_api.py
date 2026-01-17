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


@pytest.mark.api
def test_search_product_without_payload(api_client):
    response = api_client.post("/searchProduct")

    assert response.status_code == 200
    assert "products" not in response.json()


@pytest.mark.api
def test_search_returns_relevant_products(api_client):
    search_term = "panda"

    response = api_client.post("/searchProduct", data={"search_product": search_term})
    assert response.status_code == 200

    products = response.json()["products"]

    for product in products:
        assert search_term.lower() in product["name"].lower()


@pytest.mark.api
def test_search_with_empty_string(api_client):
    response = api_client.post("/searchProduct", data={"search_product": ""})

    assert response.status_code == 200
    products = response.json()["products"]

    assert len(products) == 0
