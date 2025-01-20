# app/routers/doctor_router.py

from fastapi import APIRouter
from app.schemas.doctor_schema import PatientSymptoms
from app.services.gemini_service import call_llm
from app.utils.prompts import doctor_prompt

router = APIRouter()  # Define the router here

@router.post("/symptoms", tags=["Doctor"])
def get_diagnosis(patient: PatientSymptoms):
    """
    This route processes patient symptoms and provides diagnostic suggestions.
    """
    prompt: str = doctor_prompt(
        symptoms=patient.symptoms,
        language=patient.language
    )
    response: str = call_llm(prompt)
    return {"diagnosis": response}
