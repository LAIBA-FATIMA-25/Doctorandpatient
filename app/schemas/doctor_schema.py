from pydantic import BaseModel

class PatientSymptoms(BaseModel):
    symptoms: str
    language: str | None = "en"  # Default language is English
