import pytest
import json
from jsonschema import validate


@pytest.mark.api
def test_get_all_products(api_client):
    response = api_client.get("/productsList")

    assert response.status_code == 200

    data = response.json()
    assert data is not None
