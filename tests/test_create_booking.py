import requests

BASE_URL = "https://restful-booker.herokuapp.com"
BOOKING_ENDPOINT = f"{BASE_URL}/booking"


def test_create_booking_success():
    """Test successful booking creation."""
    payload = {
        "firstname": "Jan",
        "lastname": "Kowalski",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-12-12",
            "checkout": "2025-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.post(BOOKING_ENDPOINT, json=payload, headers=headers)

    assert response.status_code == 200, f"Expetected status code: 200 but got: {response.status_code}"
    response_data = response.json()
    assert "bookingid" in response_data, "Response missing bookingid"
    assert response_data["booking"]["firstname"] == "Jan"
    assert response_data["booking"]["lastname"] == "Kowalski"
    assert response_data["booking"]["totalprice"] == 111
    assert response_data["booking"]["depositpaid"] == True
    assert response_data["booking"]["bookingdates"]["checkin"] == "2024-12-12"
    assert response_data["booking"]["bookingdates"]["checkout"] == "2025-01-01"
    assert response_data["booking"].get("additionalneeds") == "Breakfast"


def test_create_booking_missing_fields():
    """Test booking creation with missing required fields."""
    payload = {}  # Empty payload
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.post(BOOKING_ENDPOINT, json=payload, headers=headers)
    assert response.status_code == 500, f"Expetected status code: 500 but got: {response.status_code}"


def test_create_booking_checkout_before_checkin():
    """
    Test booking creation where checkout date is earlier than checkin date.
    """
    payload = {
        "firstname": "Jan",
        "lastname": "Kowalski",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2019-01-01",
            "checkout": "2018-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.post(BOOKING_ENDPOINT, json=payload, headers=headers)
    assert response.status_code == 400, f"Expetected status code: 400 but got: {response.status_code}"

def test_create_booking_invalid_first_name():
    """Test booking creation with first name type"""
    payload = {
        "firstname": 123,
        "lastname": "Kowalski",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-12-12",
            "checkout": "2025-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.post(BOOKING_ENDPOINT, json=payload, headers=headers)
    assert response.status_code == 500, f"Expetected status code: 500 but got: {response.status_code}"

def test_create_booking_invalid_last_name():
    """Test booking creation with last name type"""
    payload = {
        "firstname": "Jan",
        "lastname": 123,
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-12-12",
            "checkout": "2025-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.post(BOOKING_ENDPOINT, json=payload, headers=headers)
    assert response.status_code == 500, f"Expetected status code: 500 but got: {response.status_code}"

def test_create_booking_invalid_dates():
    """Test booking creation with invalid date formats."""
    payload = {
        "firstname": "Jan",
        "lastname": "Kowalski",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "xyz",
            "checkout": "xyz"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.post(BOOKING_ENDPOINT, json=payload, headers=headers)
    assert response.status_code == 400, f"Expetected status code: 400 but got: {response.status_code}"


def test_create_booking_invalid_price():
    """Test booking creation with invalid price type"""
    payload = {
        "firstname": "Jan",
        "lastname": "Kowalski",
        "totalprice": "money",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-12-12",
            "checkout": "2025-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.post(BOOKING_ENDPOINT, json=payload, headers=headers)
    assert response.status_code == 400, f"Expetected status code: 400 but got: {response.status_code}"


def test_create_booking_invalid_deposit():
    """Test booking creation with invalid deposit type"""
    payload = {
        "firstname": "Jan",
        "lastname": "Kowalski",
        "totalprice": 111,
        "depositpaid": "xyz",
        "bookingdates": {
            "checkin": "2024-12-12",
            "checkout": "2025-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.post(BOOKING_ENDPOINT, json=payload, headers=headers)
    assert response.status_code == 400, f"Expetected status code: 400 but got: {response.status_code}"