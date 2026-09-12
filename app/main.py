from fastapi import FastAPI, HTTPException
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
    exercise_data = exercise.model_dump()
    exercise_data["id"] = len(exercises) + 1

    exercises.append(exercise_data)

    return {
        "message": "Exercício cadastrado com sucesso!",
        "exercise": exercise_data
    }


@app.put("/exercises/{exercise_id}")
def update_exercise(exercise_id: int, exercise: Exercise):
    for item in exercises:
        if item["id"] == exercise_id:
            item["name"] = exercise.name
            item["muscle_group"] = exercise.muscle_group

            return {
                "message": "Exercício atualizado com sucesso!",
                "exercise": item
            }

    raise HTTPException(status_code=404, detail="Exercício não encontrado")


@app.delete("/exercises/{exercise_id}")
def delete_exercise(exercise_id: int):
    for item in exercises:
        if item["id"] == exercise_id:
            exercises.remove(item)

            return {"message": "Exercício excluído com sucesso!"}

    raise HTTPException(status_code=404, detail="Exercício não encontrado")