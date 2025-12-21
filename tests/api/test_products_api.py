import pytest
import pytest_playwright


@pytest.mark.api
def test_get_all_products(api_request_context):
    # api_request_context fixture is provided by pytest-playwright when pytest-playwright is installed.
    # alternative: use requests if you prefer.
    url = "https://automationexercise.com/api/productsList"
    resp = api_request_context.get(url)
    assert resp.status == 200

    data = resp.json()
    # The response structure should contain product list — adapt the assertion if necessary
    assert isinstance(data, dict) or isinstance(data, list)
    # Example check: ensure there is at least one product (structure can vary)
    # If API returns dict with 'products' key:
    if isinstance(data, dict) and "products" in data:
        assert len(data["products"]) > 0
    else:
        # If it's a list, assert non-empty
        assert len(data) > 0
