from clients.api_client import APIClient
from httpx import Response
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.exercises.exercises_schema import (GetExercisesQuerySchema, CreateExerciseRequestSchema,
                                                UpdateExerciseRequestSchema, CreateExerciseResponseSchema,
                                                GetExerciseResponseSchema, UpdateExerciseResponseSchema)


class ExercisesClient(APIClient):
    """Клиент для работы с /api/v1/exercises"""

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """Метод получения упражнений по айди курса"""
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_one_exercise_api(self, exercise_id: str) -> Response:
        """Метод получения упражнения по айди"""
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """Метод создания упражнения"""
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """Метод обновления упражнения по айди"""
        return self.patch(
            f"/api/v1/exercises/{exercise_id}",
            json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """Метод удаления упражнения по айди"""
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExerciseResponseSchema:
        response = self.get_exercises_api(query)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_one_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_one_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(
            self,
            exercise_id: str,
            request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))
