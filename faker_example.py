from faker import Faker

fake = Faker('ru_RU')

print(fake.email())
print(fake.address())

data = {
    "name": fake.name(),
    "email": fake.email(),
    "age": fake.random_int(min=18, max=100)
}

print(data)