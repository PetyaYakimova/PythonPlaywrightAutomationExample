import pytest
import requests


@pytest.mark.api
def test_get_user_details_by_email(api_base_url):
    params = {
        "email": "test@test.com"
    }

    response = requests.get(
        f"{api_base_url}/getUserDetailByEmail",
        params=params
    )

    assert response.status_code == 200

    data = response.json()
    assert "user" in data
