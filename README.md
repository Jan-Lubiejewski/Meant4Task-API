# Restful-booker create booking API tests
Tests written for website [restful-booker](https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-CreateBooking) using:
- **Python v. "3.9.1"**
- **Pytest v. "8.3.4"**
- **Requests v. "2.32.3"**

## Overiew
The API test are written for CreateBooking endpoint:
    api->Booking->CreateBooking

## Dependencies and Setup
To run the tests you have to have Python 3.9.1 (or later version) installed on your machine.
- [Python installation](https://www.python.org/downloads/)

### Prerequisites
First, if you like it may be a good idea to set up virtual environment. To do so run the following commands:
```bash
    python -m venv venv
    venv\Scripts\activate # On Windows
    source venv/bin/activate # On Linux
```
Then you should install all the requirements using this command:
```bash
    pip install -r requirements.txt
```
### Running tests
To run the tests use the command below:
```bash
    pytest
```