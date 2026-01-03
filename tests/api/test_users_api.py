import pytest


@pytest.mark.api
def test_get_user_details_by_email(api_client):
    params = {
        "email": "test@test.com"
    }

    response = api_client.get(
        "/getUserDetailByEmail",
        params=params
    )

    assert response.status_code == 200

    data = response.json()
    assert "user" in data
