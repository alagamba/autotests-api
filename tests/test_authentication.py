from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema
from tools.assertions.base import assert_status_code, assert_login_response
from http import HTTPStatus
from tools.assertions.schema import validate_json_schema
import pytest


@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    public_users_client = get_public_users_client()
    authentication_client = get_authentication_client()
    request_create_user = CreateUserRequestSchema()
    public_users_client.create_user(request_create_user)
    login_request = LoginRequestSchema(
        email=request_create_user.email,
        password=request_create_user.password
    )
    login_response = authentication_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)
    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)
    login_response_schema = LoginResponseSchema.model_json_schema()
    validate_json_schema(login_response.json(), login_response_schema)
