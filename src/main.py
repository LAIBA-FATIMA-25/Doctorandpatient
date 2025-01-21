from fastapi import FastAPI
from app.routers.doctor_router import router as doctor_router
from app.routers import doctor_router

app = FastAPI(
    title="Doctor-Patient Symptom Checker API",
    description="A FastAPI-based backend that lets patients input symptoms and receive diagnostic suggestions.",
    version="1.0.0",
)

# Include the doctor routes

app.include_router(doctor_router, prefix="/doctor")

from app.routers.doctor_router import router as doctor_router  # Make sure 'router' is correctly imported

app = FastAPI()

# Include the doctor router with the correct prefix
app.include_router(doctor_router, prefix="/doctor")
