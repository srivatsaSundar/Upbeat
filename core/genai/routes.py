from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from dependencies import get_db,get_current_user
from core.user.models import User
from .models import MentalHealth
from .schema import MentalHealthSchema
from sklearn.preprocessing import LabelEncoder  
import joblib
import numpy as np
import pandas as pd


mental_health=APIRouter()

model_file_path = 'core/genai/best_model.pkl'
loaded_model = joblib.load(model_file_path)

def custom_encode(value):
  label_mappings = {
        'mood_swing': {'NO': 0, 'YES': 1},
        'optimisim': {'1 From 10': 0, '2 From 10': 1, '3 From 10': 2, '4 From 10': 3, '5 From 10': 4, '6 From 10': 5, '7 From 10': 6, '8 From 10': 7, '9 From 10': 8},
        'euphoric': {'Seldom': 0, 'Most-Often': 1, 'Usually': 2, 'Sometimes': 3},
        'exhausted': {'Sometimes': 0, 'Usually': 1, 'Seldom': 2, 'Most-Often': 3},
        'concentration': {'1 From 10': 0, '2 From 10': 1, '3 From 10': 2, '4 From 10': 3, '5 From 10': 4, '6 From 10': 5, '7 From 10': 6, '8 From 10': 7, '9 From 10': 8},
        'sexual_activity': {'1 From 10': 0, '2 From 10': 1, '3 From 10': 2, '4 From 10': 3, '5 From 10': 4, '6 From 10': 5, '7 From 10': 6, '8 From 10': 7, '9 From 10': 8},
        'aggressive_response': {'NO': 0, 'YES': 1},
        'suicidal_thoughts': {'NO': 0, 'YES': 1},
        'authority_respect': {'NO': 0, 'YES': 1},
        'sadness': {'Usually': 0, 'Sometimes': 1, 'Seldom': 2, 'Most-Often': 3}
    }
  for col, mapping in label_mappings.items():
    if value in mapping:
      return mapping[value]
  return None

def encode_categorical_features(data):
  encoded_data = {}
  for column, value in data.items():
    encoded_value = custom_encode(value)
    if encoded_value is not None:
      encoded_data[column] = encoded_value
  return encoded_data



@mental_health.post('/classify')
def mental_care(mental_care_data: MentalHealthSchema, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    try:
        data_dict = mental_care_data.dict()
        encoded_data = encode_categorical_features(data_dict)
        encoded_df = pd.DataFrame([encoded_data])
        predictions = loaded_model.predict(encoded_df)
        new_data = MentalHealth(
            user_id=user.id,
            mood_swing=data_dict['mood_swing'],
            optimisim=data_dict['optimisim'],
            euphoric=data_dict['euphoric'],
            exhausted=data_dict['exhausted'],
            concentration=data_dict['concentration'],
            sexual_activity=data_dict['sexual_activity'],
            aggressive_response=data_dict['aggressive_response'],
            suicidal_thoughts=data_dict['suicidal_thoughts'],
            authority_respect=data_dict['authority_respect'],
            sadness=data_dict['sadness'],
            prediction=predictions[0]
        )
        db.add(new_data)
        db.commit()

        return {"predictions": predictions[0]}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")
