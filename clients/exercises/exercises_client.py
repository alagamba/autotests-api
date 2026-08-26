from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class GetExercisesQueryDict(TypedDict):
    """Описание структуры запроса на получения упражнений"""
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """Описание структуры запроса на создание упражнения"""
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int | None
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """Описание структуры запроса на изменение упражнения"""
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class Exercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int | None
    description: str
    estimatedTime: str


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на получение задания.
    """
    exercise: Exercise


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на получение списков заданий.
    """
    exercises: list[Exercise]


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на получение задания.
    """
    exercise: Exercise


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на обновление задания.
    """
    exercise: Exercise


class ExercisesClient(APIClient):
    """Клиент для работы с /api/v1/exercises"""

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """Метод получения упражнений по айди курса"""
        return self.get("/api/v1/exercises", params=query)

    def get_one_exercise_api(self, exercise_id: str) -> Response:
        """Метод получения упражнения по айди"""
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """Метод создания упражнения"""
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """Метод обновления упражнения по айди"""
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """Метод удаления упражнения по айди"""
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def get_one_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        response = self.get_one_exercise_api(exercise_id)
        return response.json()

    def update_exercise(self, exercise_id: str) -> UpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))
