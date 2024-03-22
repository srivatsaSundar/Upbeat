from datetime import date
from pydantic import BaseModel
from typing import Optional, Union

class ProfileCreate(BaseModel):
    dob: date 
    gender: str 
    appointment_frequency: str

class DoctorCreate(BaseModel):
    name: Optional[str]=None
    phone_number: Optional[str]=None
    clinic_or_hospital_name: Optional[str]=None
    email: Optional[str]=None

class EmergencyContactCreate(BaseModel):
    contact_name: str
    contact_phone_number: str
    contact_relationship: str
    