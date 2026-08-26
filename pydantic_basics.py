from pydantic import BaseModel, Field, HttpUrl, EmailStr


class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CourseSchema(BaseModel):
    id: str
    title: str
    max_score: int | None = Field(default=None, alias="maxScore")
    min_Score: int | None = Field(default=None, alias="minScore")
    preview_file: FileSchema = Field(alias="previewFile")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")


course_default_model = CourseSchema(
    id="course-1",
    title="Playwright",
    maxScore=100,
    previewFile=FileSchema(
        id="file_id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses"
    ),
    minScore=4,
    description="DEsc example",
    estimatedTime="YYY",
    createdByUser=UserSchema(
        id="user_id",
        lastName="Bond",
        firstName="James",
        middleName="Jackson",
        email="user@gmail.com"
    )
)

print("Course default model: ", course_default_model)

course_dict = {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "previewFile": {
        "id": "file_id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "description": "string",
    "estimatedTime": "string",
    "createdByUser": {
        "id": "user_id",
        "lastName": "Bond",
        "firstName": "James",
        "middleName": "Jackson",
        "email": "user@gmail.com"
    }
}

course_model_dict = CourseSchema(**course_dict)
print(course_model_dict)

course_json = """
{
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "previewFile": {
        "id": "file_id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "description": "string",
    "estimatedTime": "string",
    "createdByUser": {
        "id": "user_id",
        "lastName": "Bond",
        "firstName": "James",
        "middleName": "Jackson",
        "email": "s@gmail.com"
    }
}
"""

course_json_model = CourseSchema.model_validate_json(course_json)
print(course_json_model)
print(course_json_model.model_dump(by_alias=True))
print(course_json_model.model_dump_json(by_alias=True))
