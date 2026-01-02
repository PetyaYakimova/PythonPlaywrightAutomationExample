import pytest


@pytest.mark.api
def test_get_all_brands(api_client):
    response = api_client.get("/brandsList")

    assert response.status_code == 200

    data = response.json()
    assert "brands" in data
    assert len(data["brands"]) > 0
