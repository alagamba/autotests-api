import time
from typing import TypedDict
import httpx
from httpx import Response

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """Описание структуры запросы на создание пользователя"""
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """Клиент для работы с /api/v1/users"""

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """Метод создания нового пользователя"""
        get_random_email = f"test{time.time}@example.com"
        return self.post("/api/v1/users", json=request)
