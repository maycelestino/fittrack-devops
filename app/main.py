from fastapi import FastAPI

app = FastAPI(
    title="FitTrack API",
    description="API para gerenciamento de treinos.",
    version="1.0.0"
)

exercises = []


@app.get("/")
def home():
    return {"message": "FitTrack API funcionando!"}


@app.get("/exercises")
def list_exercises():
    return exercises


@app.post("/exercises")
def create_exercise(exercise: dict):
    exercises.append(exercise)

    return {
        "message": "Exercício cadastrado com sucesso!",
        "exercise": exercise
    }