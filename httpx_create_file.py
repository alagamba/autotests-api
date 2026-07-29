import httpx
from tools.fakers import get_random_email

loaded_data = {
    "filename": "image.png",
    "directory": "courses"
}

files = {
    "upload_file": open('./testdata/files/IMG_1790_copy.PNG', 'rb')
}
base_url = "http://127.0.0.1:8000"
create_user_url = base_url + "/api/v1/users"
payload = {
    "email": get_random_email(),
    "password": "123456",
    "lastName": "Testov",
    "firstName": "Test",
    "middleName": "Testovich"
}

create_user_response = httpx.post(create_user_url, json=payload)
create_user_response_data = create_user_response.json()

login_payload = {
    "email": payload["email"],
    "password": payload["password"]
}

login_response = httpx.post(base_url + "/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login data", login_response_data)

create_file_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

create_file_response = httpx.post(
    base_url + "/api/v1/files", data=loaded_data, files=files, headers=create_file_headers
)

create_file_response_data = create_file_response.json()
print('Create file data: ', create_file_response_data)