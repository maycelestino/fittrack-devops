from fastapi import FastAPI

app = FastAPI(
    title="FitTrack API",
    description="API para gerenciamento de treinos.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "FitTrack API funcionando!"}