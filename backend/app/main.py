from fastapi import FastAPI
from app.api.reservations import router as reservations_router

app = FastAPI()

app.include_router(reservations_router)

@app.get("/")
def root():
    return {"status": "ok", "message": "API is running"}

@app.get("/health")
def health_check():
    return {"status": "alive"}