import pytest
import json
from jsonschema import validate
from utils.paths import get_schema_path


@pytest.mark.api
def test_get_all_products(api_client):
    response = api_client.get("/productsList")

    assert response.status_code == 200

    data = response.json()
    assert data is not None

    schema_path = get_schema_path("products_schema.json")

    with open(schema_path) as f:
        schema = json.load(f)

    validate(instance=data, schema=schema)


@pytest.mark.api
def test_products_have_required_fields(api_client):
    response = api_client.get("/productsList")
    assert response.status_code == 200

    products = response.json()["products"]

    # Validate structure of the first product
    product = products[0]

    required_fields = ["id", "name", "price", "brand", "category"]

    for field in required_fields:
        assert field in product
