import httpx

# проходим авторизацию
login_payload = {
    "email": "123321@example.com",
    "password": "123456"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(login_response_data)

# Инициализируем клиент с авторизацией
client = httpx.Client(
    base_url="http://127.0.0.1:8000",
    timeout=100,
    headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
)

# Выполняем запрос с авторизацией
get_user_me_response = client.get("/api/v1/users/me")
get_user_me_data = get_user_me_response.json()
print("This user's info: ", get_user_me_data)