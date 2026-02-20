import uuid


def unique_email():
    return f"test_{uuid.uuid4().hex[:8]}@test.com"


def user_data():
    return {
        "name": "Test User",
        "email": unique_email(),
        "password": "Password123!",
        "first_name": "Test",
        "last_name": "User",
        "address": "123 Test Street",
        "country": "United States",
        "state": "California",
        "city": "Los Angeles",
        "zipcode": "90001",
        "mobile": "1234567890"
    }
