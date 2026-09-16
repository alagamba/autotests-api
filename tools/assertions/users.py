from clients.users.user_schema import CreateUserResponseSchema, CreateUserRequestSchema
from tools.assertions.base import assert_eq


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_eq(response.user.email, request.email, "email")
    assert_eq(response.user.last_name, request.last_name, "last_name")
    assert_eq(response.user.first_name, request.first_name, "first_name")
    assert_eq(response.user.middle_name, request.middle_name, "middle_name")
