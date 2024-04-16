from datetime import date
from pydantic import BaseModel
from typing import Optional, Union


class MentalHealthSchema(BaseModel):
    mood_swing: str
    optimisim: str
    euphoric: str
    exhausted: str
    concentration: str
    sexual_activity: str
    aggressive_response: str
    suicidal_thoughts: str
    authority_respect: str
    sadness: str

class MentalSchema(BaseModel):
    mood_swing: str
    optimisim: str
    euphoric: str
    exhausted: str
    concentration: str
    sexual_activity: str
    aggressive_response: str
    suicidal_thoughts: str
    authority_respect: str
    sadness: str
    prediction: str