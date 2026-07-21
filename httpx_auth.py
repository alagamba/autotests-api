import httpx

login_payload = {
    "email": "123321@example.com",
    "password": "123456"
}
base_url = "http://127.0.0.1:8000"
auth_url = base_url + "/api/v1/authentication/login"
refresh_url = base_url + "/api/v1/authentication/refresh"
get_user_info_url = base_url + "/api/v1/users/me"
login_response = httpx.post(auth_url, json=login_payload)
login_response_data = login_response.json()

print("Login response: ", login_response_data)
print("Status code", login_response.status_code)

refresh_payload = {"refreshToken": login_response_data['token']['refreshToken']}
refresh_response = httpx.post(refresh_url, json=refresh_payload)
refresh_response_data = refresh_response.json()
print(refresh_response_data)
print("Refresh response", refresh_response_data)
print("Status code", refresh_response.status_code)

auth_header = {"Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"}

get_user_information = httpx.get(get_user_info_url, headers=auth_header)
print(get_user_information.headers)
print(get_user_information.json())

