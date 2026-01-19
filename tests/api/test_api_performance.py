import pytest
import time


@pytest.mark.api
def test_products_api_response_time(api_client):
    start = time.time()
    response = api_client.get("/productsList")
    duration = time.time() - start

    assert response.status_code == 200
    assert duration < 2  # seconds
