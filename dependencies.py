from database import SessionLocal
from fastapi import Depends
from core.user.bearer import JWTBearer
from core.user.models import User
from config import get_settings
import jwt

settings=get_settings()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token:str = Depends(JWTBearer()))-> User:
    try:
        payload=jwt.decode(token,f'{settings.SECRET_KEY}',algorithms=['HS256'])
        user_id=payload.get('sub')
        db=SessionLocal()
        return db.query(User).filter(User.id==user_id).first()
    except(jwt.PyJWTError.AttributeError):
        return HTTPExceptions(status_code="Invaild token")
