from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="FitTrack API",
    description="API para gerenciamento de treinos.",
    version="1.0.0"
)


class Exercise(BaseModel):
    name: str
    muscle_group: str


exercises = []


@app.get("/")
def home():
    return {"message": "FitTrack API funcionando!"}


@app.get("/exercises")
def list_exercises():
    return exercises


@app.post("/exercises")
def create_exercise(exercise: Exercise):
    exercises.append(exercise.model_dump())

    return {
        "message": "Exercício cadastrado com sucesso!",
        "exercise": exercise
    }