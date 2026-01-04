from fastapi import FastAPI
from fastapi import FastAPI
from app.api.reservations import router as reservations_router

app = FastAPI()

app.include_router(reservations_router)

@app.get("/health")
def health_check():
    return {"status": "alive"}