import pytest
import requests


@pytest.mark.api
def test_get_all_brands(api_base_url):
    response = requests.get(f"{api_base_url}/brandsList")

    assert response.status_code == 200

    data = response.json()
    assert "brands" in data
    assert len(data["brands"]) > 0
