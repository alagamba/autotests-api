import json

data = {
    "name": "Мария",
    "age": 25,
    "is_student": True
}

data_object = json.dumps(data, ensure_ascii=False, indent=2)
print(data_object)


data_2 = '{"name": "Мария", "age": 25, "is_student": true}'

parsed_json = json.loads(data_2)
print(parsed_json)