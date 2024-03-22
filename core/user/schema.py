from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    phone_number: str
    password: str

class UserLogin(BaseModel):
    email:str
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str