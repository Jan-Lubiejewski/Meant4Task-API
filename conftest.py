import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.fixture(scope="session")
def auth_token():
    """Fetch and return an authentication token."""
    url = f"{BASE_URL}/auth"
    payload = {"username": "admin", "password": "password123"}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200, "Failed to fetch auth token"

    token = response.json().get("token")
    assert token, "Token not found in response"
    
    return token