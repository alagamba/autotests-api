from pydantic import BaseModel, Field, HttpUrl, ConfigDict


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    model_config = ConfigDict(populate_by_name=True)

    file_name: str = Field(alias="filename")
    directory: str
    upload_file: str


class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    id: str
    file_name: str = Field(alias="filename")
    directory: str
    url: HttpUrl


class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    file: FileSchema
