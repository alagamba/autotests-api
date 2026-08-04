from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response


class GetExercisesQueryDict(TypedDict):
    """Описание структуры запроса на получения упражнений"""
    courseId: str


class CreateExerciseQueryDict(TypedDict):
    """Описание структуры запроса на создание упражнения"""
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int | None
    description: str
    estimatedTime: str


class UpdateExerciseQueryDict(TypedDict):
    """Описание структуры запроса на изменение упражнения"""
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """Клиент для работы с /api/v1/exercises"""

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """Метод получения упражнений по айди курса"""
        return self.get("/api/v1/exercises", params=query)

    def get_one_exercise_api(self, exercise_id: str) -> Response:
        """Метод получения упражнения по айди"""
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseQueryDict) -> Response:
        """Метод создания упражнения"""
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseQueryDict) -> Response:
        """Метод обновления упражнения по айди"""
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """Метод удаления упражнения по айди"""
        return self.delete(f"/api/v1/exercises/{exercise_id}")
