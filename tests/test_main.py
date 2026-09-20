from fastapi.testclient import TestClient

from app.main import app, exercises

client = TestClient(app)


def setup_function():
    exercises.clear()


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "FitTrack API funcionando!"}


def test_create_exercise():
    response = client.post(
        "/exercises",
        json={
            "name": "Supino reto",
            "muscle_group": "Peito"
        }
    )

    assert response.status_code == 200
    assert response.json()["exercise"]["name"] == "Supino reto"
    assert response.json()["exercise"]["id"] == 1


def test_list_exercises():
    client.post(
        "/exercises",
        json={
            "name": "Rosca direta",
            "muscle_group": "Bíceps"
        }
    )

    response = client.get("/exercises")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Rosca direta"


def test_update_exercise():
    client.post(
        "/exercises",
        json={
            "name": "Supino reto",
            "muscle_group": "Peito"
        }
    )

    response = client.put(
        "/exercises/1",
        json={
            "name": "Supino inclinado",
            "muscle_group": "Peito"
        }
    )

    assert response.status_code == 200
    assert response.json()["exercise"]["name"] == "Supino inclinado"


def test_delete_exercise():
    client.post(
        "/exercises",
        json={
            "name": "Agachamento",
            "muscle_group": "Pernas"
        }
    )

    response = client.delete("/exercises/1")

    assert response.status_code == 200
    assert response.json() == {"message": "Exercício excluído com sucesso!"}


def test_exercise_not_found():
    response = client.delete("/exercises/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Exercício não encontrado"}

def test_create_exercise_without_muscle_group():
    response = client.post(
        "/exercises",
        json={
            "name": "Supino reto"
        }
    )

    assert response.status_code == 422


def test_update_exercise_not_found():
    response = client.put(
        "/exercises/999",
        json={
            "name": "Supino inclinado",
            "muscle_group": "Peito"
        }
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Exercício não encontrado"
    }