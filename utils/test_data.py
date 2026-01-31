import uuid


def unique_email():
    return f"test_{uuid.uuid4().hex[:8]}@test.com"


def user_data():
    return {
        "name": "Test User",
        "email": unique_email(),
        "password": "Password123!"
    }
