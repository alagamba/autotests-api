import httpx
from tools.fakers import get_random_email

base_url = "http://127.0.0.1:8000"
create_user_url = base_url + "/api/v1/users"
payload = {
    "email": get_random_email(),
    "password": "123456",
    "lastName": "Testov",
    "firstName": "Test",
    "middleName": "Testovich"
    }

response = httpx.post(create_user_url, json=payload)
print(response.status_code)
print(response.json())