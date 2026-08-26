from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str
    zipcode: str


class User(BaseModel):
    id: int = 0
    name: str
    email: str = "huy@huy.ru"
    is_active: bool = False


user = User(
    id=2,
    name="Zhopa",

    address=Address(city="Nswisa", zipcode="3333")
)

print(user.model_dump_json())
